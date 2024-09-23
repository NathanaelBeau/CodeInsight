def test(A: list, B: list) -> list:
    return [i for i, val in enumerate(A) if val in B]

