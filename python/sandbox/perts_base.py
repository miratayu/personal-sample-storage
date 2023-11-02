import logging
from abc import ABCMeta, abstractmethod

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PertsBase(metaclass=ABCMeta):
    """ perts Base """
    def __init__(self):
        """ init """
        self.log_head = "[PertsBase]"

    @abstractmethod
    def assembly(self):
        """ assembly """
        ...

    @abstractmethod
    def aaa(self):
        """ aaa """
        pass
