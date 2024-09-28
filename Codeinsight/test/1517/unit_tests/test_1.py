dict0 = {'one': 10, 'two': 5, 'three': 7}
expected_result =  {'two': 5, 'three': 7, 'one': 10}
result = test(dict0)
assert result == expected_result, 'Test failed'