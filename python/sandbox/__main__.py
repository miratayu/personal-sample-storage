import sys
import logging

import sandbox

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info(f"python version: {sys.version_info}")
    logger.info(f"isPythonVersionOver3.8: {sys.version_info>=(3, 8)}")
    logger.info("sandbox main")
    # sample_runs()
    # inequality_sign()
    # file_operations_runs()
    # contents_runs()
    # sample_001()
    # check_validation()
    # sandbox.summary_configs()
    # sandbox.sort_timestamp()
    # sandbox.dict_partition({})
    sandbox.list_dict_integration()
    logger.info(not [])
    logger.info("end sandbox main")
