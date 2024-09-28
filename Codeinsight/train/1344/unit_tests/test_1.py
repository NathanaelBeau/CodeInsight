arr0 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
expected_result =  np.array([[10, 11], [13, 14]])
assert np.array_equal(test(arr0), expected_result), 'Test failed'