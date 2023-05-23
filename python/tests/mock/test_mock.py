from sandbox import sandbox


def _checker(expected: bool, actual: bool) -> None:
    """ checker """
    assert actual is expected


def test_mock(mocker):
    mocker.patch("sandbox.sandbox.sample_checker", return_value=False)
    result = sandbox.sample_checker(True, True)
    print(result)
    _checker(False, result)
