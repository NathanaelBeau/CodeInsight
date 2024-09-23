lst0 = [{'id': 'A', 'val': 100}, {'id': 'B', 'val': 200}, {'id': 'A', 'val': 150}]
expected_result =  [{'id': 'A', 'val': 100}, {'id': 'B', 'val': 200}]
assert test(lst0) == expected_result, 'Test failed'