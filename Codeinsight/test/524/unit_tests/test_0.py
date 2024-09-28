arr0 = np.array([True, False, True, False, True])
expected_result =  (np.array([0, 2, 4]),)
assert np.array_equal(test(arr0), expected_result), 'Test failed'