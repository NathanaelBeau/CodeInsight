arr0 = np.array([1, 2, 3, 4, 5])
n0 = 2
expected_result =  [np.array([1, 2, 3]), np.array([4, 5])]
result = test(arr0, n0)
assert all([np.array_equal(r, e) for r, e in zip(result, expected_result)]), 'Test failed'