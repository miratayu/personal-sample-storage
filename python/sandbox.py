import logging

from util_pack import sample
from util_pack import file_operations

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


def file_operation() -> None:
    """ file operation """
    logger.info(f"file_operation")
    text = "*****link*****\nabc\ndef\nghi\n*****start*****hogehogepiyopiyo*****end*****\n"
    text2 = [
        "## :warning: *****WARNING***** :warning:\n", "warning text\n", "*****link*****\n",
        "jkl\n", "abc\n", "mno\n", "ghi\n", "pqr\n", "*****start*****hogehoge*****end*****\n"
    ]
    text3 = [
        "## :warning: *****WARNING***** :warning:\n", "warning text\n", "*****link*****\n",
        "jkl\n", "abc\n", "mno\n", "ghi\n", "pqr\n", "*****start*****piyopiyo*****end*****\n"
    ]
    file_operations.write_file("test_sample.txt", text)
    file_operations.write_file("test_sample_2.txt", text2)
    file_operations.write_file("test_sample_3.txt", text3)
    file_operations.consolidate_files_duplicate_deletion(r"test_sample*.txt")


if __name__ == '__main__':
    logger.info("sandbox")
    # sample_runs()
    file_operation()
    # inequality_sign()
