def test(test_string: str, str0: str) -> int:
    try:
        return test_string.rindex(str0)
    except ValueError:
        return -1

