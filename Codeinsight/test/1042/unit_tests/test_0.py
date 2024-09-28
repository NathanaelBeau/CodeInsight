lst0 = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}, {'id': 1, 'name': 'Doe'}]
expected_result =  [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
assert test(lst0) == expected_result, 'Test failed'