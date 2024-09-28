bool_array0 = np.array([True, False, True, False, True])
expected_result =  np.array([0, 2, 4])
result = test(bool_array0)
assert np.array_equal(result, expected_result), 'Test failed'