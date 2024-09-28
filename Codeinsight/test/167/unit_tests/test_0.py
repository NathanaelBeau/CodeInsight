lst0 = [{'id': 2, 'name': 'B'}, {'id': 1, 'name': 'A'}, {'id': 3, 'name': 'C'}]
lst1 = [1, 2, 3]
expected_result =  [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}, {'id': 3, 'name': 'C'}]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'