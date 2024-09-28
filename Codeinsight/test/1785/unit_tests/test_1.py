lst0 = ['name', 'age', 'city']
lst1 = ['John', 25, 'New York']
expected_result =  {'name': 'John', 'age': 25, 'city': 'New York'}
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'