arr0 = np.array([[10, 2, 30], [40, 50, 6], [70, 8, 90]])
axis0 = 1
expected_result =   np.array([2, 1, 2])
result = test(arr0, axis0)
assert np.array_equal(result, expected_result), 'Test failed'