lst0 = np.array([])
lst1 = np.array([12, 13])
expected_result =  np.array([12, 13])
result = test(lst0, lst1)
assert np.array_equal(result, expected_result), 'Test failed'