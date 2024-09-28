arr0 = np.array([1, 2, 4, 5, 7])
expected_result =  [np.array([1, 2]), np.array([4, 5]), np.array([7])]
result = test(arr0)
assert all([np.array_equal(r, e) for r, e in zip(result, expected_result)]), 'Test failed'