arr0 = np.array([0, 0, 1, 1, 1, 0])
expected_result =  (2 + 3 + 4) / 3
result = test(arr0)
assert np.isclose(result, expected_result), 'Test failed'