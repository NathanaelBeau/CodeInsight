lst0 = [{'value': 1, 'other': 'a'}, {'value': 2, 'other': 'b'}, {'not_value': 3}]
expected_result =  [1, 2]
result = test(lst0)
assert result == expected_result, 'Test failed'