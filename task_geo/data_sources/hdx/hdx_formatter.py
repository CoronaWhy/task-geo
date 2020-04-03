import logging

logger = logging.getLogger(__name__)


def acap_formatter(raw):
    data = raw.copy()
    data.columns = [column.lower() for column in data.columns]
    data = data.drop(['id', 'pcode', 'admin_level_name', 'link', 'alternative source'], axis=1)
    logger.info('\n %s', data.head())
    return data
