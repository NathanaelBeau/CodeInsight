arr0 = np.array([0, 0, 0, 1])
expected_result =  3
result = test(arr0)
assert np.isclose(result, expected_result), 'Test failed'