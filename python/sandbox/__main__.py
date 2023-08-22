import logging

import sandbox

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("sandbox main")
    # sample_runs()
    # inequality_sign()
    # file_operations_runs()
    # contents_runs()
    # sample_001()

    # check_validation()

    # sandbox.summary_configs()
    # sandbox.sort_timestamp()

    sandbox.dict_partition({
        "name": "test_*",
        "@timestamp": "now-1d",
        "timestamp": {"gte": "now-7d", "lt": "now-1h"},
        "number": 1,
        "flg": True,
        "message": "sample"
    })

    logger.info("end sandbox main")
