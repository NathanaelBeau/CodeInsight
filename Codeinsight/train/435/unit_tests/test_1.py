lst0 = [1, 1, 1, 1]
lst1 = ['a', 'a', 'a', 'a']
expected_codes = np.array([0, 0, 0, 0])
result = test('col1', 'col2', lst0, lst1)
assert (result == expected_codes).all(), 'Test failed'