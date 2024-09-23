dict0 = {"a": 1, "b": 2, "c": {"d": 4, "e": {"f": 5}}}
expected_result =  6
result = test(dict0)
assert result == expected_result, 'Test failed'