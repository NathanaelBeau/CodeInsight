dict0 = {'name': 'John', 'age': 30}
dict1 = {'city': 'New York', 'country': 'USA'}
expected_output = {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
assert test(dict0, dict1) ==expected_output, 'Test failed'