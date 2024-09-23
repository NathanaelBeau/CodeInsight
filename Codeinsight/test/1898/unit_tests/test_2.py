arr0 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
lst0 = [0, 1]
lst1 = [1, 3]
expected_result =  np.array([[2, 4], [6, 8]])
assert np.array_equal(test(arr0, lst0, lst1), expected_result), 'Test failed'