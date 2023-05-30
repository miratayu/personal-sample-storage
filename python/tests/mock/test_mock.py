from sandbox import sandbox
from util_pack import sample


def _checker(expected: bool, actual: bool) -> None:
    """ checker """
    assert actual is expected


def test_mock(mocker):
    """ test sample mock """
    mocker.patch("sandbox.sandbox.sample_checker", side_effect=[False, True])
    result = sandbox.sample_checker(True, True)
    print(result)
    _checker(False, result)
    result = sandbox.sample_checker(True, False)
    print(result)
    _checker(True, result)


def test_mock_sandbox(mocker):
    """ test mock sandbox """
    mock_sample_util = mocker.Mock()
    mock_sample_util.gamma = mocker.Mock(return_value=[4, 5, 6])
    mock_sample = mocker.Mock()
    mock_sample.create = mocker.Mock(return_value=mock_sample_util)
    sandbox_obj = sandbox.Sandbox(mock_sample)
    sandbox_obj.run()
