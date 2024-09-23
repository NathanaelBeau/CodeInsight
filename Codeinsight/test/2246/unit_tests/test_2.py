dict0 = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": {"g": 4}}}}
expected_result =  7
result = test(dict0)
assert result == expected_result, 'Test failed'