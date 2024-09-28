lst0 = [{'id': 'apple', 'color': 'red'}, {'id': 'banana', 'color': 'yellow'}, {'id': 'apple', 'color': 'green'}]
expected_result =  [{'id': 'apple', 'color': 'red'}, {'id': 'banana', 'color': 'yellow'}]
assert test(lst0) == expected_result, 'Test failed'