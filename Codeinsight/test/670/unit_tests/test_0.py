arr0 = np.array([1, 2, 0, 3, 0, 4])
expected_result =  (np.array([2, 4]),)
result = test(arr0)
assert np.array_equal(result[0], expected_result[0]), 'Test failed'