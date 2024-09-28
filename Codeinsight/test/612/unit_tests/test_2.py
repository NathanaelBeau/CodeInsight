lst0 = [{'var0': 'value1', 'key2': 'value2'}, {'key3': 'value4', 'key4': 'value5'}]
expected_result =  [{'key2': 'value2'}, {'key3': 'value4', 'key4': 'value5'}]
result = test(lst0)
assert result == expected_result, 'Test failed'