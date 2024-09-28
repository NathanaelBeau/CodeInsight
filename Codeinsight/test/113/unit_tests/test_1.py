dict0 = {'key1': 'value1'}
expected_result =  {'key1': 'value1', 'dict3': {'spam': 5, 'ham': 6}}
result = test(dict0)
assert result == expected_result, 'Test failed'