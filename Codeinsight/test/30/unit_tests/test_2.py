lst0 = [{'name': 'John', 'age': 30}, {'city': 'New York'}, {'age': 25}]
expected_output = {'name', 'age', 'city'}
assert test(lst0) == expected_output, 'Test failed'