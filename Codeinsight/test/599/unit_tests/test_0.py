lst0 = [{'key': 'value1'}, {'key': 'value2'}, {'not_key': 'value3'}]
var0 = 'key'
expected_result =  ['value1', 'value2']
result = test(lst0, var0)
assert result == expected_result, 'Test failed'