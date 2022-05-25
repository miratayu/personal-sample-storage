import logging

from util_pack import sample
from util_pack import file_operations

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def sample_runs() -> None:
    logger.info(f'test1: {sample.test1(sample.add)}')
    sample.run_open(sample.open_step)
    sample.run(sample.run_step_one, sample.run_step_two, a=1, b=3)
    sample.load_json_file()

    logger.info(f'sample.printer: {sample.printer()}')


if __name__ == '__main__':
    logger.info('sandbox')
    # sample_runs()
    text = "abc\ndef\nghi\n"
    text2 = ["## :warning: **WARNING** :warning:\n", "warning text\n", "jkl\n", "abc\n", "mno\n", "ghi\n", "pqr\n"]
    file_operations.write_file("test_sample.txt", text)
    file_operations.write_file("test_sample_2.txt", text2)
    file_operations.consolidate_files_duplicate_deletion(r"test_sample*.txt")
