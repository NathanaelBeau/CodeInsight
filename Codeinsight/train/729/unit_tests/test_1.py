lst0 = [{'id': 2, 'name': 'B'}, {'id': 1, 'name': 'A'}, {'id': 3, 'name': 'C'}]
lst1 = [3, 2, 1]
expected_result =  [{'id': 3, 'name': 'C'}, {'id': 2, 'name': 'B'}, {'id': 1, 'name': 'A'}]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'