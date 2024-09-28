def test(d0: dict) -> dict:
    return {k: 'updated' for k, v in d0.items() if v is not None}
