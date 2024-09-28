dct0 = {'key': 'value', 'another_key': 'another_value'}
var0 = 'key'
expected_result =  {'another_key': 'another_value'}
result = test(dct0, var0)
assert result == expected_result, 'Test failed'