dict0 = {'a': True, 'b': 10, 'c': "Hello", 'd': False}
expected_result =  False  # One of the boolean values is false
result = test(dict0)
assert result == expected_result, 'Test failed'