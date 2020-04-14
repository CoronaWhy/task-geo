from datetime import datetime, timedelta
import os

import fitz
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

CATEGORIES = [
    "Retail & recreation",
    "Grocery & pharmacy",
    "Parks",
    "Transit stations",
    "Workplaces",
    "Residential"
]

MOBILITY_REPORTS_URL = "https://www.google.com/covid19/mobility/"


def find_pdf_files_list(download_folder):
    """Conect to google mobility report and download the links to the PDF reports."""

    response = requests.get(MOBILITY_REPORTS_URL)
    soup = BeautifulSoup(response.text, features='lxml')

    list_pdf = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href[-4:] == '.pdf':
            date = href[41:51]
            country_iso2 = href[52:54]

            # distinction between country report or specific region report
            if len(href) == 77:
                list_pdf.append({
                    'date': pd.to_datetime(date).date(),
                    'country_iso': country_iso2,
                    'region': np.nan,
                    'href': href,
                    'path': f"{download_folder}/{date}_{country_iso2}.pdf"
                })
            else:
                region = href[55:-23].replace("_", " ")
                list_pdf.append({
                    'date': pd.to_datetime(date).date(),
                    'country_iso': country_iso2,
                    'region': region,
                    'href': href,
                    'path': f"{download_folder}/{date}_{country_iso2}_{href[55:-23]}.pdf"
                })

    return list_pdf


def download_pdf_files(pdf_files, skip_downloaded=True):
    for row in pdf_files:
        if skip_downloaded and os.path.exists(row['path']):
            continue

        with open(row['path'], 'wb') as fp:
            response = requests.get(row['href'])
            fp.write(response.content)


def parse_stream(stream):
    data = []
    transformation_parameters = None
    for line in stream.splitlines():
        if line.endswith(" cm"):
            # parameters to transform from the stream to the actual position
            # on the pdf page
            transformation_parameters = list(map(float, line.split()[:-1]))
        elif line.endswith(" rg"):
            # not sure what this is
            continue
        elif line.endswith(" l") or line.endswith(" m"):
            # (x, y) coordinates in the object
            # m denotes the start of a new 'block' of points
            data.append(list(map(float, line.split()[:2])))
        else:
            continue

    if not data:
        return data, 0, 0, 0

    data = np.array(data)

    # The baseline of the graph (y=0)
    baseline = data[0, 1]

    # The points in data first draw the x axis (x increasing) and then draw
    # the graph, reversed (x decreasing)
    # the last point goes back to the origin of the graph
    data = data[int(len(data) / 2):-1]
    data = np.flip(data, axis=0)
    data[:, 1] = -(data[:, 1] - baseline)

    # graph height
    max_y = baseline
    # length of a single day
    dx = data[1, 0]
    return data, dx, max_y, transformation_parameters


def extract_graph(pdf, graph_name, region, xref, date):
    stream = pdf.xrefStream(xref[0]).decode()
    xref_data, dx_xref, max_y_xref, transformation_parameters = parse_stream(stream)
    if not len(xref_data):
        return pd.DataFrame(columns=['date', graph_name])

    # Parameters to recover the actual data
    first_date = datetime(2020, 2, 23)
    max_y = 80

    dates = [
        first_date + timedelta(days=int(round(x / dx_xref))) for x in xref_data[:, 0]]
    mobility = xref_data[:, 1] * max_y / max_y_xref

    data_graph = pd.DataFrame({
        'date': dates,
        graph_name: mobility
    })

    return data_graph


def get_region_indices(page_text):
    """Given the list of texts from a PDF page, return the region names."""
    indices = {}
    first_index = 0  # This is because the region name is the title of the section
    indices[first_index] = page_text[first_index]
    # Residential is the last section, we count also the summary line.
    if 'Residential' in page_text:
        term = 'Residential'
    else:
        term = 'Residential '  # Case when there is not ennoght data

    second_index = page_text.index(term) + 2
    indices[second_index] = page_text[second_index]
    return indices


def get_region_name(index, region_indices):
    dict_index = max([key for key in region_indices.keys() if key <= index])
    return region_indices[dict_index]


def extract_page(pdf, page_number, country_iso, date):
    page_text = pdf.getPageText(page_number).splitlines()

    info_in_page = []
    if page_number >= 2:
        region_indices = get_region_indices(page_text)

    for (index, line) in enumerate(page_text):
        if line in CATEGORIES:
            if page_number >= 2:
                region = get_region_name(index, region_indices)
            else:
                region = country_iso

            info_in_page.append((line, region))

    xrefs = sorted(pdf.getPageXObjectList(page_number), key=lambda x: int(x[1].replace("X", "")))

    graph_columns = {}
    for (graph_name, region), xref in zip(info_in_page, xrefs):
        data_graph = extract_graph(pdf, graph_name, region, xref, date)
        if region not in graph_columns:
            graph_columns[region] = []

        graph_columns[region].append(data_graph)

    return graph_columns


def structure_results(result):
    structured = {}

    for item in result:
        for key in item:
            if key not in structured:
                structured[key] = []
            structured[key].extend(item[key])

    return structured


def extract_country(path, country_iso, region, date):
    pdf = fitz.Document(path)

    results = []
    length_document = len(list(pdf.pages())) - 1
    for page_number in range(length_document):
        results.append(extract_page(pdf, page_number, country_iso, date))

    structured = structure_results(results)

    first_date = datetime(2020, 2, 23).date()
    last_date = date
    template = pd.DataFrame({
        'country_iso2': country_iso,
        'date': [
            first_date + timedelta(days=d) for d in range((last_date - first_date).days + 1)]
    })
    template['date'] = pd.to_datetime(template['date'])

    merged = []
    for key in structured:
        main = template.copy()
        for column in structured[key]:
            main = main.merge(column, how='left', on='date')
            main['region'] = key

        merged.append(main)

    return pd.concat(merged)


def extract_pdfs(pdf_files):
    result = []

    for row in pdf_files:
        del row['href']
        result.append(extract_country(**row))

    return pd.concat(result)


def mobility_connector(download_folder, download=True, skip_downloaded=True):
    pdf_files = find_pdf_files_list(download_folder)

    if download:
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        download_pdf_files(pdf_files, skip_downloaded)
    return extract_pdfs(pdf_files)
