bool_array0 = np.array([True, True, True, True])
expected_result =  np.array([0, 1, 2, 3])
result = test(bool_array0)
assert np.array_equal(result, expected_result), 'Test failed'