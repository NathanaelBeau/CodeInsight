lst0 = [{'id': 2, 'name': 'B'}, {'id': 1, 'name': 'A'}, {'id': 3, 'name': 'C'}, {'id': 4, 'name': 'D'}]
lst1 = [4, 1, 3, 2]
expected_result =  [{'id': 4, 'name': 'D'}, {'id': 1, 'name': 'A'}, {'id': 3, 'name': 'C'}, {'id': 2, 'name': 'B'}]
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'