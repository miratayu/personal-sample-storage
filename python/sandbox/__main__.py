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

    count: int = 5
    test_source = None
    # test_source = {"sand": "test_1"}
    for i in range(count):
        logger.info(f"count: {i}")
        if test_source is None:
            logger.info("test_source is None")
            continue
        if not sandbox.validation(test_source):
            logger.info("validation false")
            continue
        logger.info("SUCCESS")

    logger.info("end sandbox main")
