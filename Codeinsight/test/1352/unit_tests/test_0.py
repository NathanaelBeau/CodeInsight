lst0 = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20},
    ]
expected_output = {'name', 'age'}
assert test(lst0) ==expected_output, 'Test failed'