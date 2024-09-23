arr0 = np.array([True, False, True, False])
expected_result =  (np.array([0, 2]),)
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'