lst0 = [{"a": 1, "b": 2}, {"a": 1, "b": 2}, {"a": 2, "b": 3}]
expected_result =  [{"a": 1, "b": 2}, {"a": 2, "b": 3}]
assert test(lst0) == expected_result, 'Test failed'