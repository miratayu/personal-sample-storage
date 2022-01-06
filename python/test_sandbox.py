import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestSandBox:

    @pytest.mark.SandBox
    def test_sand_box(self, request):
        logger.info(f'request: {request}')
        logger.info(f'type(request): {type(request)}')
        pass

