def test(the_list: str, n: int) -> list:
    return [the_list[i:i+n] for i in range(0, len(the_list), n)]

