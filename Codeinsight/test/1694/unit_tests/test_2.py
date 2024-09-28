arr0 = np.array([[1, 20, 3], [4, 15, 6], [7, 10, 9]])
axis0 = 0
expected_result =  np.array([2, 0, 2])
result = test(arr0, axis0)
assert np.array_equal(result, expected_result), 'Test failed'