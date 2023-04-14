import logging

from util_pack import sample
from util_pack import file_operations
from util_pack import contents

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def inequality_sign() -> None:
    min_count = 10
    max_count = 10
    current_count = 10
    logger.info(f"current_count > min_count:{current_count > min_count}")
    logger.info(f"current_count >= min_count:{current_count >= min_count}")
    logger.info(f"current_count <= max_count:{current_count <= max_count}")
    logger.info(f"current_count < max_count:{current_count < max_count}")


def sample_runs() -> None:
    """ sample runs """
    logger.info(f"sample_runs")
    logger.info(f"test1: {sample.test1(sample.add)}")
    sample.run_open(sample.open_step)
    sample.run(sample.run_step_one, sample.run_step_two, a=1, b=3)
    sample.load_json_file()

    logger.info(f'sample.printer: {sample.printer()}')


def file_operations_runs() -> None:
    """ sample runs """
    file_operations.run()


def contents_runs() -> None:
    """ sample runs """
    contents.load()


def move() -> None:
    x = 1
    y = 1
    vy = {}
    vx = {}
    ar = {}

    for i in range(4):
        for j in range(4):
            for k in range(4):
                ny = y + vy[ar[k]]
                nx = x + vx[ar[k]]


def sample_001() -> None:
    repeat: int = 0
    data_list = ["a", "b", "c"]
    for i in range(repeat):
        logger.info(f"count: {i}")

    result_list = data_list * repeat
    logger.info(f"result_list: {result_list}")


def key_checker(target: any, key: str) -> any:
    """ key checker """
    value = None
    try:
        value = target[key]
    except KeyError as e:
        logger.error(f"not key is {e}")
    return value


def validation(source) -> bool:
    """ validation """
    if key_checker(source, "test") is None:
        return False
    return True


if __name__ == '__main__':
    logger.info("sandbox")
    # sample_runs()
    # inequality_sign()
    # file_operations_runs()
    # contents_runs()
    # sample_001()

    count: int = 5
    test_source = None
    # test_source = {"sand": "test_1"}
    for i in range(count):
        logger.info(f"count: {i}")
        if test_source is None:
            logger.info("test_source is None")
            continue
        if not validation(test_source):
            logger.info("validation false")
            continue
        logger.info("SUCCESS")

    logger.info("end sandbox")
