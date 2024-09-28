arr0 = np.array([10, 20, 30, 40, 50])
idx0 = np.array([3, 0, 4, 1, 2])
expected_result =  np.array([40, 10, 50, 20, 30])
result = test(arr0, idx0)
assert np.array_equal(result, expected_result), 'Test failed'