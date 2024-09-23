arr0 = np.array([-1, 0, 1, 2, 3])
threshold0 = 0
expected_result =  np.array([1, 2, 3])
result = test(arr0, threshold0)
assert np.array_equal(result, expected_result), 'Test failed'