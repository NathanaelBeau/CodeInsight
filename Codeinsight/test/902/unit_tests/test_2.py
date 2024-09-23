dict0 = {'name': 'John'}
dict1 = {'age': 25, 'city': 'London'}
expected_result =  {'name': 'John', 'age': 25, 'city': 'London'}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'