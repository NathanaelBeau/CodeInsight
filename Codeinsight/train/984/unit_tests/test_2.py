arr0 = np.array([[9.5, 10.4], [11.3, 12.2]])
expected_result =  np.array([[9, 10], [11, 12]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'