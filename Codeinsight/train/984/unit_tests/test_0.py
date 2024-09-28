arr0 = np.array([[1.1, 2.2], [3.3, 4.4]])
expected_result =  np.array([[1, 2], [3, 4]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'