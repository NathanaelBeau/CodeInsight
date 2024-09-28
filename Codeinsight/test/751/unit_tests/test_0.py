lst0 = [3, 1, 2]
lst1 = ['C', 'A', 'B']
expected_output = ([3, 2, 1], ['C', 'B', 'A'])
assert test(lst0, lst1) == expected_output, 'Test failed'