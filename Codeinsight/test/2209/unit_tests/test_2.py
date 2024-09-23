lst0 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
lst1 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
expected_result =  np.outer(lst0[0], lst1[0]) + np.outer(lst0[1], lst1[1])
result = test(lst0, lst1)
assert np.array_equal(result, expected_result), 'Test failed'