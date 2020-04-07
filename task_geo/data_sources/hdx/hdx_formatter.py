import logging

logger = logging.getLogger(__name__)


def acap_formatter(raw):
    data = raw.copy()
    data.columns = [column.lower() for column in data.columns]
    data = data.drop(['pcode', 'admin_level_name', 'alternative source'], axis=1)
    column_order = ['id', 'country', 'region', 'iso', 'category', 'measure',
                    'targeted_pop_group', 'comments', 'non_compliance', 'date_implemented',
                    'source', 'source_type', 'entry_date', 'link']
    data = data[column_order]
    return data
