arr0 = np.array([0.5, 1.5, 2.5, 3.5])
expected_result =  np.array([0, 1, 2, 3])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'