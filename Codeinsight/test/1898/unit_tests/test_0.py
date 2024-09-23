arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
lst0 = [0, 2]
lst1 = [1, 2]
expected_result =  np.array([[2, 3], [8, 9]])
assert np.array_equal(test(arr0, lst0, lst1), expected_result), 'Test failed'