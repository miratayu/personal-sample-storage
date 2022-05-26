import os
import logging
import glob

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def write_file(file_name: str, text: any) -> None:
    """ write file """
    logger.info(f"write file")
    logger.info(f"type(text): {type(text)}")
    if os.path.exists(file_name):
        os.remove(file_name)
    try:
        if isinstance(text, str):
            with open(file_name, "w", encoding="UTF-8") as file:
                file.write(text)
        elif isinstance(text, list):
            with open(file_name, "w", encoding="utf-8", newline="\n") as file:
                file.writelines(text)
    except Exception as exception:
        logger.info(f"{file_name} write exception: {exception}")


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
            result_list += load_file.readlines()
    logger.info(f"result_list: {result_list}")

    warning_head = split_str_list(result_list, "## :warning: ")
    warning_text = split_str_list(warning_head["unmatch"], "warning text")
    warnings = list(dict.fromkeys(warning_head["match"] + warning_text["match"]))
    logger.info(f"warnings: {warnings}")

    links = split_str_list(warning_text["unmatch"], "*****link*****")
    link = list(dict.fromkeys(links["match"]))
    logger.info(f"link: {link}")

    others = links["unmatch"]
    logger.info(f"others: {others}")

    result = warnings + link + others
    logger.info(f"result: {result}")

    write_file("consolidate.txt", result)


def split_str_list(str_list: list, search_text: str) -> dict:
    """ split str_list """
    logger.info(f"split str_list")
    return {
        "match": [s for s in str_list if s.startswith(search_text)],
        "unmatch": [s for s in str_list if not s.startswith(search_text)]
    }
