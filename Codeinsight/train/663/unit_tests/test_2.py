arr0 = np.array([0, 0, 0])
expected_result =  (np.array([0, 1, 2]),)
result = test(arr0)
assert np.array_equal(result[0], expected_result[0]), 'Test failed'