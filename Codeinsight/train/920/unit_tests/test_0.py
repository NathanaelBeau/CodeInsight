dict0 = {'name': 'John', 'age': 30, 'gender': 'male'}
expected_result =  {'name', 'age', 'gender'}
result = test(dict0)
assert result == expected_result, 'Test failed'