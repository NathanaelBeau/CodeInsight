arr0 = np.array([False, False, False, False])
expected_result =  (np.array([]),)
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'