import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def data_info(data, key) -> str:
    value = data_checker(data, key)
    return f"{key}: {value}"


def data_checker(data, key) -> str:
    value = None
    try:
        value = data[key]
    except KeyError as e:
        logger.error(f"Key does not exist: {e}")
    return value


def join_items(data):
    result = ''
    for key, value in data.items():
        result += ','
        result += f'({key}:{value})'
    result = result.replace(',', '', 1)
    logger.info(result)


if __name__ == '__main__':
    logger.info('sandbox')
    with open('contents_list.json') as load_file:
        test_file = json.load(load_file)
    logger.info(f'test_file: {test_file}')
    for index, current in enumerate(test_file['list']):
        logger.info(f'index: {index}, current: {current}')
        logger.info(data_info(current, 'title'))
        join_items(current['item'])
