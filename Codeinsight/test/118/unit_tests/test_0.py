lst0 = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
expected_result =  {'a': 1, 'b': 3, 'c': 4}
result = test(lst0)
assert result == expected_result, 'Test failed'