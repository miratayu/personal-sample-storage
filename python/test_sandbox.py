import pytest
import logging

from _pytest.fixtures import FixtureRequest

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestSandBox:

    @pytest.mark.SandBox
    def test_sand_box(self, request: FixtureRequest):
        logger.info(f'request: {request}')
        logger.info(f'type(request): {type(request)}')
        logger.info(f'test name: {request.node.name}')

