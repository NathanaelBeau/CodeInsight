lst0 = np.array([7, 8])
lst1 = np.array([9, 10, 11])
expected_result =  np.array([7, 8, 9, 10, 11])
result = test(lst0, lst1)
assert np.array_equal(result, expected_result), 'Test failed'