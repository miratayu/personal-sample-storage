import logging

from utility import sample
from utility import file_operations
from utility import contents

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def inequality_sign() -> None:
    """ inequality sign """
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
    """ move """
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
    """ sample 001 """
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


def sample_checker(expected: bool, actual: bool) -> bool:
    """ sample checker """
    return actual is expected


def check_validation() -> None:
    """ check validation """
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


def summary_configs() -> None:
    """ summary configs """
    test_source = [
        {"name": "abc", "number": 1},
        {"name": "abc", "number": 2},
        {"name": "abc", "number": 3},
        {"name": "def", "number": 1},
        {"name": "def", "number": 2},
        {"name": "def", "number": 3},
        {"name": "xyz", "number": 1},
        {"name": "xyz", "number": 1},
        {"name": "xyz", "number": 1},
        {"name": "xyz", "number": 999},
    ]
    test_config = {}
    for source in test_source:
        name = source['name']
        number = source['number']
        try:
            numbers = test_config[name].get("numbers")
        except Exception as e:
            logger.debug(e)
            numbers = []
        numbers.append(number)
        test_config[name] = {"numbers": list(set(numbers))}
    logger.info(f"test_config: {test_config}")


def sort_timestamp() -> None:
    """ sort timestamp """
    test_source = [
        {"timestamp": "2023-08-02T01:23:45.678Z", "score": 9},
        {"timestamp": "2023-08-05T12:34:56.789Z", "score": 8},
        {"timestamp": "2023-08-01T01:23:45.678Z", "score": 7},
        {"timestamp": "2023-08-05T01:23:45.678Z", "score": 6},
        {"timestamp": "2023-08-04T12:34:56.789Z", "score": 5},
        {"timestamp": "2023-08-01T12:34:56.789Z", "score": 4},
        {"timestamp": "2023-08-02T12:34:56.789Z", "score": 3},
        {"timestamp": "2023-08-03T01:23:45.678Z", "score": 2},
        {"timestamp": "2023-08-03T12:34:56.789Z", "score": 1},
        {"timestamp": "2023-08-04T01:23:45.678Z", "score": 0},
    ]
    test_source.sort(key=lambda x: x['timestamp'], reverse=True)
    logger.info(f"test_source: {test_source}")
    logger.info(f"test_source[0]['timestamp']: {test_source[0]['timestamp']}")
    assert test_source[0]['timestamp'] == "2023-08-05T12:34:56.789Z"


def dict_partition(params: dict) -> None:
    """ dict partition """
    if params == {}:
        params = {
            "name": "test_*",
            "@timestamp": "now-1d",
            "timestamp": {"gte": "now-7d", "lt": "now-1h"},
            "number": 1,
            "flg": True,
            "message": "sample",
            "exists": "keyword"
        }
    result = []
    for key, value in params.items():
        logger.info(f"key: {key}, value: {value}, type(value): {type(value)}")
        current_item = pattern_match(key, value)
        logger.info(f"current_item: {current_item}")
        result.append(current_item)
    logger.info(f"result: {result}")


def pattern_match(key: str, value: any) -> dict:
    """ pattern match """
    timestamp = {
        "normal": {"range": {key: value}},
        "string": {"range": {key: {"gte": value, "lt": "now"}}}
    }
    pattern = {
        "name": {
            "normal": {"match": {key: value}},
            "wildcard": {"wildcard": {key: value}}
        },
        "exists": {
            "normal": {"exists": {"field": value}}
        },
        "timestamp": timestamp,
        "@timestamp": timestamp
    }
    result = {"match": {key: value}}
    state = "normal"

    try:
        if key == "exists":
            pass
        elif "*" in value:
            state = "wildcard"
        elif type(value) is str:
            state = "string"
        result = pattern[key][state]
    except Exception as e:
        logger.warning(e)
        if state == "string":
            result = {"match": {f"{key}.keyword": value}}
    return result


def list_dict_integration() -> None:
    """ list_dict_integration """
    source = [
        {"code": "BEL", "type": "fast", "id": 1, "name": "abc", "score": 123, "tag": "sample"},
        {"code": "GEL", "type": "slow", "id": 2, "name": "def", "score": 456, "tag": "sample"},
        {"code": "BEL", "type": "fast", "id": 3, "name": "ghi", "score": 789, "tag": "sample"}
    ]
    target = [
        {"code": "BEL", "type": "fast", "id": 1, "name": "abc", "score": 321, "tag": "temple"},
        {"code": "BEL", "type": "fast", "id": 2, "name": "def", "score": 654, "tag": "temple"},
        {"code": "GEL", "type": "fast", "id": 3, "name": "ghi", "score": 987, "tag": "temple"}
    ]
    contents_value = {
        "source": source,
        "target": target
    }
    result_list = []
    for i in contents_value["source"]:
        result = {}
        for j in contents_value["target"]:
            if i["code"] != j["code"]:
                continue
            if i["type"] != j["type"]:
                continue
            if i["id"] != j["id"]:
                continue
            result = {
                "code": i["code"],
                "id": i["id"],
                "source_tag": i["tag"],
                "target_tag": j["tag"],
                "source_score": i["score"],
                "target_score": j["score"]
            }
        if not result:
            continue
        logger.info(f"result: {result}")
        result_list.append(result)

    logger.info(f"result_list: {result_list}")


def list_dict_duplicate() -> None:
    """ list_dict_duplicate """
    logger.info('sandbox.list_dict_duplicate')

    def has_duplicates(seq: list) -> bool:
        return len(seq) != len(set(seq))

    data_list = [
        {'data': 123},
        {'data': 456},
        {'data': 789},
        {'data': 123},
        {'data': 789},
        {'data': 789},
        {'data': 789},
    ]
    values_list = []
    for data in data_list:
        values_list.append(data.get('data'))
    logger.info(f"values_list: {values_list}")
    is_duplicate = has_duplicates(values_list)
    logger.info(f"is_duplicate: {is_duplicate}")
    if is_duplicate:
        logger.info(f"!!!!!duplicate error!!!!!")


def poc_check() -> None:
    """ poc_check """
    data = {'test': 123, 'prime': 456}
    index: str = 'test'
    logger.info(data[index])
    logger.info(not [])

    test_data = ['a', 'b', 'c', 'd', 'e']
    logger.info(f"test_data: {test_data}")
    for i, current in enumerate(test_data):
        logger.info(f"index: {i}, current: {current}")
        result = test_data[0]
        logger.info(f"result: {result}")
        if result in test_data:
            # test_data.remove(result)
            test_data.append(i)
            logger.info(f"test_data: {test_data}")
        if i > 20:
            break

    test_list = ['a', 'b', 'c', 'd', 'e']
    target_data = 'c'
    result_list = [item for item in test_list if target_data in item]
    logger.info(f"result_list: {result_list}")

    empty_list = []

    if empty_list is None:
        logger.info(f"list is None")
    if not empty_list:
        logger.info(f"list is empty")
    logger.info(f"empty_list: {empty_list}")


class Sandbox:
    """ class sandbox """

    def __init__(self, sample_impl: sample.Sample) -> None:
        """ init """
        self.log_head = "[Sandbox]"
        self.sample_create = sample_impl.create()

    def run(self) -> None:
        """ run """
        logger.info(f"{self.log_head} run")
        self._process()
        self._result()

    def _process(self) -> None:
        """ process """
        logger.info(f"{self.log_head} process")
        self.sample_create.alpha()

    def _result(self) -> None:
        """ result """
        logger.info(f"{self.log_head} result")
        self.sample_create.beta()
        self._view()

    def _view(self) -> None:
        """ view """
        logger.info(f"{self.log_head} view")
        gamma_list = self.sample_create.gamma()
        logger.info(f"{self.log_head} gamma_list: {gamma_list}")
        logger.info(f"{self.log_head} len(gamma_list): {len(gamma_list)}")
