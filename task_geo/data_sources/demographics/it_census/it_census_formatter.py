TRANSLATED_COLUMNS = {
    'Codice comune': 'city_code',
    'Denominazione': 'city',
    'Età': 'age',
    'Maschi celibi': 'single_men',
    'Maschi coniugati': 'married_males',
    'Maschi divorziati': 'divorced_males',
    'Maschi vedovi': 'widowed_males',
    'Maschi uniti civilmente': 'males_civil_union',
    'Maschi già in unione civile (per scioglimento)': 'males_civil_union_dissolution',
    'Maschi già in unione civile (per decesso del partner)': "males_civil_union_death",
    'Totale Maschi': 'total_males',
    'Femmine nubili': 'single_females',
    'Femmine coniugate': 'married_females',
    'Femmine divorziate': 'divorced_females',
    'Femmine vedove': 'female_widows',
    'Femmine unite civilmente': 'females_united_civilly',
    'Femmine già in unione civile (per scioglimento)': 'females_civil_union_dissolution',
    'Femmine già in unione civile (per decesso del partner)': "females_civil_union_death",
    'Totale Femmine': 'total_females'
}


def it_census_formatter(raw):
    return raw.rename(columns=TRANSLATED_COLUMNS)
