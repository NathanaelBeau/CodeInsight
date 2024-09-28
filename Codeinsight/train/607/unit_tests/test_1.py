arr0 = np.array(['7.7', '8.8'])
expected_result =  np.array([7.7, 8.8])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'