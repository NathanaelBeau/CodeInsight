lst0 = [
        {'name': 'Alice', 'age': 25, 'city': 'New York'},
        {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
        {'name': 'Charlie', 'age': 20, 'city': 'Boston'},
    ]
expected_output = {'name', 'age', 'city'}
assert test(lst0) ==expected_output, 'Test failed'