arr0 = np.array([[1, 2, 3], [4, 5, 6]])
lst0 = [7, 8, 9]
expected_result =  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = test(arr0, lst0)
assert np.array_equal(result, expected_result), 'Test failed'