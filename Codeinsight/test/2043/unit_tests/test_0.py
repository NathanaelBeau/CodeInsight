arr0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
axis0 = 1
expected_result =  np.array([2, 2, 2])
result = test(arr0, axis0)
assert np.array_equal(result, expected_result), 'Test failed'