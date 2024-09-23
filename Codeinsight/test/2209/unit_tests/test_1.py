lst0 = [np.array([1]), np.array([2])]
lst1 = [np.array([3]), np.array([4])]
expected_result =  np.outer(lst0[0], lst1[0]) + np.outer(lst0[1], lst1[1])
result = test(lst0, lst1)
assert np.array_equal(result, expected_result), 'Test failed'