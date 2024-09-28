arr0 = np.array([[5.9, 6.8], [7.7, 8.6]])
expected_result =  np.array([[5, 6], [7, 8]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'