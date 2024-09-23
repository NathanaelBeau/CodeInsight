dict1 = {"a1": 1, "a10": 2, "a2": 3, "b1": 4}
expected_output = ["a1", "a2", "a10", "b1"]
assert test(dict1) == expected_output, 'Test failed'