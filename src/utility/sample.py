import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def printer() -> str:
    text = "sample"
    print(text)
    return text


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


def load_json_file(file_name: str = 'resource/contents_list.json') -> None:
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


def run_step_one() -> None:
    logger.info(f'run_step_one')


def run_step_two() -> None:
    logger.info(f'run_step_two')


def run(*run_steps, a=0, b=1) -> None:
    repeat_count = 3
    logger.info(f'a: {a}')
    logger.info(f'b: {b}')
    for run_step in run_steps:
        for count in range(repeat_count):
            logger.info(f'count: {count+1} / {repeat_count}')
            run_step()


class SampleUtil:
    """ class sample utility """
    def __init__(self) -> None:
        """ init """
        self.log_head = "[SampleUtil]"

    def alpha(self) -> None:
        """ alpha """
        logger.info(f"{self.log_head} alpha")

    def beta(self) -> None:
        """ beta """
        logger.info(f"{self.log_head} beta")

    def gamma(self) -> list:
        """ gamma """
        logger.info(f"{self.log_head} gamma")
        return [1, 2, 3]


class Sample:
    """ class sample """

    def __init__(self) -> None:
        """ init """
        self.log_head = "[Sample]"

    def create(self):
        """ create """
        logger.info(f"{self.log_head} sample create")
        sample_util = SampleUtil()
        return sample_util

    def view(self) -> None:
        """ view """
        logger.info(f"{self.log_head} sample view")
