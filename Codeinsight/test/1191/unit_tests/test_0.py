arr0 = np.array([1, 2, 3, 4, 5, 2])
val0 = 2
expected_result =  np.array([1, 3, 4, 5])
assert np.array_equal(test(arr0, val0), expected_result), 'Test failed'