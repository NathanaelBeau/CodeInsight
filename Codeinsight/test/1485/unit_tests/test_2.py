arr0 = np.array([5, 8, 6, 7])
expected_result =  np.array([1, 3, 2, 0])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'