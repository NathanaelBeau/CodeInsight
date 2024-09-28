lst0 = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4, 'c': 5}]
expected_result =  {'a': 4, 'b': 6, 'c': 5}
assert test(lst0) == expected_result, 'Test failed'