dict0 = {'p': {'count': 100}, 'q': {'count': 50}, 'r': {'count': 100}}
expected_result =  'p'
result = test(dict0)
assert result == expected_result, 'Test failed'