lst0 = [1, 2, 3]
lst1 = ['a', 'b', 'c']
selector = [0, 1, 0, 1, 0, 1]
expected_output = [1, 'a', 2, 'b', 3, 'c']
assert list(test([lst0, lst1], selector)) == expected_output, 'Test failed'