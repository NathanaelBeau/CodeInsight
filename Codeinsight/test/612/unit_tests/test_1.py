lst0 = [{'var0': 'value1'}, {'key3': 'value4'}]
expected_result =  [{}, {'key3': 'value4'}]
result = test(lst0)
assert result == expected_result, 'Test failed'