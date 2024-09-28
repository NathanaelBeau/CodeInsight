arr0 = np.array([5, 6])
expected_result =  np.array([[5], [6]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'