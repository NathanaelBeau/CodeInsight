arr0 = np.array([True, True, True])
expected_result =  (np.array([0, 1, 2]),)
assert np.array_equal(test(arr0), expected_result), 'Test failed'