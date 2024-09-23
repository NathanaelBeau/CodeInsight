lst0 = np.array([-1000, -2, 0, 2, 4, 1000])
expected_result =  np.array([-2, 0, 2, 4])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'