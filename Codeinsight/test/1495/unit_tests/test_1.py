lst0 = [('name', 'Alice'), ('age', 30), ('city', 'New York')]
expected_result =  {'name': 'Alice', 'age': 30, 'city': 'New York'}
result = test(lst0)
assert result == expected_result, 'Test failed'