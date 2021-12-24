import logging
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def data_info(data: dict, key: str) -> str:
    value = data_checker(data, key)
    return f"{key}: {value}"


def data_checker(data: dict, key: str) -> str:
    value = None
    try:
        value = data[key]
    except KeyError as e:
        logger.error(f"Key does not exist: {e}")
    return value


def join_items(data: dict) -> None:
    result = ''
    for key, value in data.items():
        result += ','
        result += f'({key}:{value})'
    result = result.replace(',', '', 1)
    logger.info(result)


def load_json_file(file_name: str = 'contents_list.json') -> None:
    with open(file_name) as load_file:
        test_file = json.load(load_file)
    logger.info(f'test_file: {test_file}')
    for index, current in enumerate(test_file['list']):
        logger.info(f'index: {index}, current: {current}')
        logger.info(data_info(current, 'title'))
        join_items(current['item'])


def save_text(text: str = "") -> None:
    if not text:
        logger.info(f'None')
    if text:
        text += "-"
    result_text = text + "result.txt"
    logger.info(f'{result_text}')


def add(a, b):
    return a+b


def test1(func):
    logger.info(f'{type(func)}')  # <class 'function'>
    return func(1, 2)


def open_step() -> None:
    logger.info('step1')
    logger.info('step2')
    logger.info('step3')


def run_open(func) -> None:
    logger.info('run_open')
    func()


if __name__ == '__main__':
    logger.info('sandbox')

    logger.info(f'test1: {test1(add)}')
    run_open(open_step)

