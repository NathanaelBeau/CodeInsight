arr0 = np.array([1, 2, 3, 4, 5])
expected_result =  (np.array([]),)
result = test(arr0)
assert np.array_equal(result[0], expected_result[0]), 'Test failed'