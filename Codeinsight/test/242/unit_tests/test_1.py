dict0 = {'name': 'John', 'age': 30}
dict1 = {'age': 30, 'name': 'John'}
expected_output = True
assert test(dict0, dict1) == expected_output, 'Test failed'