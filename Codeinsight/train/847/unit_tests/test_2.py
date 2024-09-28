arr0 = np.array([1, 2, 3, 4, 5, 6])
n0 = 4
expected_result =  [np.array([1, 2]), np.array([3, 4]), np.array([5]), np.array([6])]
result = test(arr0, n0)
assert all([np.array_equal(r, e) for r, e in zip(result, expected_result)]), 'Test failed'