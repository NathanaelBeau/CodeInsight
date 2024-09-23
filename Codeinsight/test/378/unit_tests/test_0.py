var0 = "key1=value1;key2=value2;key3=value3"
expected_result =  {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
assert test(var0) == expected_result, 'Test failed'