import logging
from sandbox.perts_base import PertsBase

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PertsA(PertsBase):
    """ perts A """
    def __init__(self):
        """ init """
        super().__init__()
        self.log_head = "[PertsA]"

    def assembly(self):
        """ assembly """
        logger.info(f"{self.log_head} assembly")

    def aaa(self):
        """ aaa """
        logger.info(f"{self.log_head} aaa")
