import requests
import pandas as pd
from pandas.tseries.offsets import DateOffset
import numpy as np
from bs4 import BeautifulSoup
import fitz
import matplotlib.pyplot as plt

import cv2

pdf_folder = "pdf_files"

# =============================================================================
# Get html of google page
# =============================================================================

base_url = "https://www.google.com/covid19/mobility/"

response = requests.get(base_url)
soup = BeautifulSoup(response.text, features='lxml')

# =============================================================================
# Find all the pdf files
# =============================================================================
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
                'country_iso2': country_iso2,
                'region': np.nan,
                'pdf_href': href,
                'pdf_path': f"{pdf_folder}/{date}_{country_iso2}.pdf"
            })
        else:
            flag = False
            region = href[55:-23].replace("_", " ")
            list_pdf.append({
                'date': pd.to_datetime(date).date(),
                'country_iso2': country_iso2,
                'region': region,
                'pdf_href': href,
                'pdf_path': f"{pdf_folder}/{date}_{country_iso2}_"
                "{href[55:-23]}.pdf"
            })

list_pdf = pd.DataFrame(list_pdf)

# =============================================================================
# Download all the pdf files
# =============================================================================
for row in list_pdf.itertuples():
    with open(row.pdf_path, 'wb') as fp:
        response = requests.get(row.pdf_href)
        fp.write(response.content)


# =============================================================================
# Function reading the stream of a PDF XObject and giving back the data of the
# graph.
# =============================================================================
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
    data = np.array(data)

    # The baseline of the graph (y=0)
    baseline = data[0, 1]

    # The points in data first draw the x axis (x increasing) and then draw
    # the graph, reversed (x decreasing)
    # the last point goes back to the origin of the graph
    data = data[int(len(data)/2):-1]
    data = np.flip(data, axis=0)
    data[:, 1] = -(data[:, 1] - baseline)
    
    # graph height
    max_y = baseline
    # length of a single day
    dx = data[1, 0]
    return data, dx, max_y, transformation_parameters

# =============================================================================
# Extract information from the pdf files
# =============================================================================
info_categories = [
    "Retail & recreation",
    "Grocery & pharmacy",
    "Parks",
    "Transit stations",
    "Workplaces",
    "Residential"
]

df_mobility = []
for row in list_pdf.itertuples():
    pdf = fitz.Document(row.pdf_path)
    
    first_date = pd.to_datetime("23feb2020").date()
    last_date = row.date
        
    pdf_data = pd.DataFrame({
        'country_iso2': row.country_iso2,
        'region': row.region,
        'date': [first_date + DateOffset(days=d) \
                 for d in range((last_date - first_date).days + 1)]
    })

    # The first two pages of the pdf contain the information about the main
    # country/region of the pdf, the (optional) subsequent pages contain
    # regions, resp. sub-regions, and the last page some notices that
    # do not contain interesting data.

    # First two pages
    for p in range(2):
        page = pdf.loadPage(p)
        
        page_text = pdf.getPageText(p).splitlines()
        
        info_in_page = []
        for line in page_text:
            if line in info_categories:
                info_in_page.append(line)
# =============================================================================
#         print("\n\n")
#         for par in page.getText('blocks'):
#             print(par)
#             
#         # transformation matrix to bring xref objects bboxes to page
#         # coordinates
#         page_mat = page.getTransformation()
#         a, b, c, d, e, f = page_mat.a, page_mat.b, page_mat.c, page_mat.d, \
#             page_mat.e, page_mat.f
# =============================================================================

# =============================================================================
#         STUFF
# =============================================================================
# =============================================================================
#         scale = 1
#         mat = fitz.Matrix(scale, scale)
#         pixmap = pdf.getPagePixmap(p, matrix=mat)
#         pixmap.writePNG(f"page{p}.png")
#         img = cv2.imread(f"page{p}.png")
#         print(img.shape)
# =============================================================================

        xrefs = sorted(pdf.getPageXObjectList(p),
                       key=lambda x: int(x[1].replace("X","")))

        for graph_name, xref in zip(info_in_page, xrefs):
            stream = pdf.xrefStream(xref[0]).decode()
            #print(stream)
# =============================================================================
#             print(stream)
#             print(pdf._getXrefString(xref[0]))
# =============================================================================
            xref_data, dx_xref, max_y_xref, transformation_parameters = \
                parse_stream(stream)
            
# =============================================================================
#             bbox_xref = xref[-1]
#             x_min, y_min, x_max, y_max = bbox_xref
#             bbox_page = [
#                 a*x_min + c*y_min + e,
#                 c*x_min + d*y_min + f,
#                 a*x_max + c*y_max + e,
#                 c*x_max + d*y_max + f
#             ]
#             print(bbox_page)
# =============================================================================
            
# =============================================================================
#             What's below is a first, raw version (that works at least
#             for now). It should be improved in the future.
# =============================================================================
            
            # Parameters to recover the actual data
            first_date = pd.to_datetime("23feb2020").date()
            last_date = row.date
            max_y = 80
            
            n_days = (last_date - first_date).days
            
            dates = [first_date + DateOffset(days=int(round(x/dx_xref)))
                     for x in xref_data[:, 0]]
            mobility = xref_data[:, 1]*max_y/max_y_xref
            
            data_graph = pd.DataFrame({
                'date': dates,
                graph_name: mobility
            })
            
            pdf_data = pdf_data.merge(data_graph, on=['date'], how='left')

    df_mobility.append(pdf_data)

df_mobility = pd.concat(df_mobility)
