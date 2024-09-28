lst0 = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]
expected_result =  {'a': {'key': 'a', 'value': 1}, 'b': {'key': 'b', 'value': 2}}
assert test(lst0) == expected_result, 'Test failed'