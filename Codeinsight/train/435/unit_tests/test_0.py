lst0 = [1, 2, 1, 3]
lst1 = ['a', 'b', 'a', 'c']
expected_codes = np.array([0, 1, 0, 2])
result = test('col1', 'col2', lst0, lst1)
assert (result == expected_codes).all(), 'Test failed'