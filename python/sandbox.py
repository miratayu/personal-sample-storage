import logging

from util_pack import sample

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info('sandbox')

    logger.info(f'test1: {sample.test1(sample.add)}')
    sample.run_open(sample.open_step)
    sample.run(sample.run_step_one, sample.run_step_two, a=1, b=3)
    sample.load_json_file()

    logger.info(f'sample.printer: {sample.printer()}')
