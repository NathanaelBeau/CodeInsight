arr0 = np.array([[10, 20], [30, 40], [50, 60]])
expected_result =  np.array([90, 120])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'