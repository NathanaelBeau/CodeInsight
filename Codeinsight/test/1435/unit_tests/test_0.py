str0 = "{'key1': 'value1', 'key2': 'value2'}"
expected_result =  {'key1': 'value1', 'key2': 'value2'}
result = test(str0)
assert result == expected_result, 'Test failed'