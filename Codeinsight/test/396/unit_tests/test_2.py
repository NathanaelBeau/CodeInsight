dict0 = {'name': 'John', 'age': 30, 'city': 'New York'}
dict1 = {'age': 25, 'city': 'London', 'country': 'UK'}
expected_result =  {'age': 30, 'city': 'New York'}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'