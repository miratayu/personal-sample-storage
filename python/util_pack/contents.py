import logging
import glob
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def load() -> None:
    """ load """
    logger.info(f"load contents")
    file_path = "resource\\contents"
    file_pattern = r"*.json"
    result = {}
    contents_files = glob.glob(file_path + "\\" + file_pattern)
    logger.info(f"contents_files: {contents_files}")

    file_list = []
    for contents_file in contents_files:
        file_list.append(contents_file + "\n")
    logger.info(f"file_list: {file_list}")
    with open('resource/output/contents_file_list.txt', 'w') as file:
        file.writelines(file_list)

    for current_file in contents_files:
        logger.info(f"current_file: {current_file}")
        with open(current_file, "r") as load_file:
            load_contents = json.load(load_file)
            result_key = current_file.replace(".json", "").replace(f"{file_path}", "").replace("\\contents_", "")
            logger.info(f"result_key: {result_key}")
            result[f"{result_key}"] = load_contents
    logger.info(f"resul: {result}")
    with open('resource/output/contents_result_list.json', 'w') as file:
        json.dump(result, file, ensure_ascii=False)
