lst0 = np.array([10, 20, 30, 40, 50, 60])
expected_result =  np.array([10, 20, 30, 50, 60])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'