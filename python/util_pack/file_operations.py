import os
import logging
import glob

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def write_file(file_name: str, text: str) -> None:
    """ write file """
    logger.info(f"write file")
    if os.path.exists(file_name):
        os.remove(file_name)
    try:
        with open(file_name, "w", encoding="UTF-8") as file:
            file.write(text)
    except Exception as exception:
        logger.info(f"{file_name} write exception: {exception}")


def writelines_file(file_name: str, lines: list) -> None:
    """ writelines file """
    logger.info(f"writelines file")
    if os.path.exists(file_name):
        os.remove(file_name)
    try:
        with open(file_name, "w", encoding="utf-8", newline="\n") as file:
            file.writelines(lines)
    except Exception as exception:
        logger.info(f"{file_name} writelines exception: {exception}")


def consolidate_files(file_pattern: str = r"*.txt") -> None:
    """ consolidate files """
    logger.info(f"consolidate files")
    result_text = ""
    result_files = glob.glob(file_pattern)
    logger.info(f"result_files: {result_files}")
    for current_file in result_files:
        logger.debug(f"current_file: {current_file}")
        with open(current_file, "r") as load_file:
            result_text += (load_file.read() + "\n")
    logger.info(f"result_text: {result_text}")
    write_file("consolidate.txt", result_text)


def consolidate_files_duplicate_deletion(file_pattern: str = r"*.txt") -> None:
    """ consolidate files """
    logger.info(f"consolidate files")
    result_list = []
    result_files = glob.glob(file_pattern)
    logger.info(f"result_files: {result_files}")
    for current_file in result_files:
        logger.debug(f"current_file: {current_file}")
        with open(current_file, "r") as load_file:
            result_list += (load_file.readlines() + ["\n"])
    logger.info(f"result_list: {result_list}")
    result = list(dict.fromkeys(result_list))
    logger.info(f"result: {result}")
    writelines_file("consolidate.txt", result)
