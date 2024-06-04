import json
import logging
from concurrent import futures
import time
import random

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ParallelPOC:
    log_head = "[ParallelPOC]"
    file_name = 'parallel_poc_conf.json'

    def download(self):
        logger.info(f"{self.log_head} download: started.")
        sleep_seconds = random.randint(10, 15)
        time.sleep(sleep_seconds)
        with open(self.file_name, 'w') as file:
            json.dump({"is_downloaded": True}, file, ensure_ascii=False)
        logger.info(f"{self.log_head} download: completed.")

    def measurement(self):
        is_downloaded = False
        start_time = time.time()
        while not is_downloaded:
            if time.time() - start_time > 20:
                logger.info(f"{self.log_head} timeout")
                break
            logger.info(f"{self.log_head} measurement: started.")
            sleep_seconds = random.randint(2, 4)
            time.sleep(sleep_seconds)
            logger.info(f"{self.log_head} measurement: ended.")
            with open(self.file_name) as load_file:
                test_file = json.load(load_file)
                is_downloaded = test_file.get("is_downloaded")
            logger.info(f"{self.log_head} is_downloaded: {is_downloaded}")
        logger.info(f"{self.log_head} measurement: completed.")

    def do_parallel(self):
        future_list = []
        with futures.ProcessPoolExecutor(max_workers=2) as executor:
            future_download = executor.submit(self.download)
            future_list.append(future_download)
            future_measurement = executor.submit(self.measurement)
            future_list.append(future_measurement)
            _ = futures.as_completed(future_list, 60)

        logger.info(f"{self.log_head} future_list: {future_list}")
        logger.info(f"{self.log_head} completed.")


if __name__ == '__main__':
    with open('parallel_poc_conf.json', 'w') as file:
        json.dump({"is_downloaded": False}, file, ensure_ascii=False)
    parallel_poc = ParallelPOC()
    parallel_poc.do_parallel()
