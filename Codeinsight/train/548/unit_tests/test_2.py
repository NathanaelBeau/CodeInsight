arr0 = np.array([10, 9, 11])
expected_result =  np.array([11, 10, 9])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'