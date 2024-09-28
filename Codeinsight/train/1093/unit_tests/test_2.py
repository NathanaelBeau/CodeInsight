lst0 = [{'name': 'John'}, {'age': 25}, {'city': 'London'}]
expected_result =  {'name': 'John', 'age': 25, 'city': 'London'}
result = test(lst0)
assert result == expected_result, 'Test failed'