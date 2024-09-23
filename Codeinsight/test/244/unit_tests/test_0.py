dict0 = { 'item1': [7, 1, 9], 'item2': [8, 2, 3], 'item3': [9, 3, 11] }
lst0 = 2
expected_output = [('item2', [8, 2, 3]), ('item1', [7, 1, 9]), ('item3', [9, 3, 11])]
assert test(dict0, lst0) ==expected_output, 'Test failed'