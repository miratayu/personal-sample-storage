import pytest
import logging

from _pytest.fixtures import FixtureRequest

from sandbox import sandbox

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestSandBox:

    @staticmethod
    def _markers(request: FixtureRequest):
        return [x.name for x in request.node.iter_markers() if "fixture" not in x.name]

    def _id(self, request: FixtureRequest):
        markers = self._markers(request)
        logger.info(f'markers: {markers}')
        ids = [marker for marker in markers if marker.lower().startswith('id')]
        return ids[0] if ids else ''

    @pytest.mark.SandBox
    @pytest.mark.id_001
    def test_sand_box(self, request: FixtureRequest):
        logger.info(f'request: {request}')
        logger.info(f'type(request): {type(request)}')
        logger.info(f'test name: {request.node.name}')
        logger.info(f'self._markers(request: {self._markers(request)}')
        logger.info(f'self._id(request): {self._id(request)}')
        test_value = {
            "test": 1
        }
        assert sandbox.validation(test_value)

    @pytest.mark.SandBox
    @pytest.mark.id_002
    def test_sand_box(self, request: FixtureRequest):
        logger.info(f'request: {request}')
        logger.info(f'type(request): {type(request)}')
        logger.info(f'test name: {request.node.name}')
        logger.info(f'self._markers(request: {self._markers(request)}')
        logger.info(f'self._id(request): {self._id(request)}')
        test_value = {
            "test": 1
        }
        test_value.update(report={})
        logger.info(f"test_value: {test_value}")
        test_value['report'].update(a={
            "isEnabled": True,
            "isPassed": False
        })
        logger.info(f"test_value: {test_value}")
        test_value['report'].update(b={
            "isEnabled": False,
            "isPassed": False
        })
        logger.info(f"test_value: {test_value}")

    @pytest.mark.SandBox
    @pytest.mark.id_003
    def test_sand_box(self, request: FixtureRequest):
        logger.info(f'request: {request}')
        flags = [True, False]
        for flg in flags:
            logger.info(f'flg: {flg}')
            if not flg:
                logger.info('early return')
                return
            logger.info('Normal return')
