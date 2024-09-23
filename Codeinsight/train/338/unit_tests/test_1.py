arr0 = np.array([1, 0, 0, 1, 0, 1])
expected_result =  (0 + 3 + 5) / 3
result = test(arr0)
assert np.isclose(result, expected_result), 'Test failed'