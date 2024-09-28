lst2 = [np.array([]), np.array([])]
expected_result =  np.array([[], []])
result = test(lst2)
assert np.array_equal(result, expected_result), 'Test failed'