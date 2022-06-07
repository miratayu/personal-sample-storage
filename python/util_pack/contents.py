import logging
import glob
import json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def load() -> None:
    """ load """
    logger.info(f"load contents")
    file_path = "resource/contents/"
    file_pattern = r"*.json"
    result = {}
    contents_files = glob.glob(file_path + file_pattern)
    logger.info(f"contents_files: {contents_files}")
    for current_file in contents_files:
        logger.info(f"current_file: {current_file}")
        with open(current_file, "r") as load_file:
            load_contents = json.load(load_file)
            result_key = current_file.replace("resource/contents\\contents_", "").replace(".json", "")
            result[f"{result_key}"] = load_contents
    logger.info(f"resul: {result}")
    with open('resource/output/contents_result_list.json', 'w') as file:
        json.dump(result, file, ensure_ascii=False)
