arr0 = np.array([0, 0.5, 0, 1.5, 2.5, 0])
expected_result =  (0.5, 2.5)
result = test(arr0)
assert result == expected_result, 'Test failed'