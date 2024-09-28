arr0 = np.array([1, 3, 4, 7, 8, 10])
expected_result =  [np.array([1]), np.array([3, 4]), np.array([7, 8]), np.array([10])]
result = test(arr0)
assert all([np.array_equal(r, e) for r, e in zip(result, expected_result)]), 'Test failed'