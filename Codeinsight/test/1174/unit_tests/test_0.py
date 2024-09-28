dict0 = {'a': {'count': 5}, 'b': {'count': 10}, 'c': {'count': 3}}
expected_result =  'b'
result = test(dict0)
assert result == expected_result, 'Test failed'