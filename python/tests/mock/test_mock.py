from sandbox import sandbox


def _checker(expected: bool, actual: bool) -> None:
    """ checker """
    assert actual is expected


def test_mock(mocker):
    mocker.patch("sandbox.sandbox.sample_checker", side_effect=[False, True])
    result = sandbox.sample_checker(True, True)
    print(result)
    _checker(False, result)
    result = sandbox.sample_checker(True, False)
    print(result)
    _checker(True, result)
