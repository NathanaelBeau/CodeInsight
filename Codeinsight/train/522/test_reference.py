def test(dict0, dict1):
    return {" ".join([dict0[char] for char in k]): v for k, v in dict1.items()}

