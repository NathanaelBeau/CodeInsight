arr0 = np.array([False, False, False])
expected_result =  tuple([np.array([])])
assert np.array_equal(test(arr0), expected_result), 'Test failed'