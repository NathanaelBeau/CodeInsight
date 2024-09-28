arr0 = np.array([0, 1, 2, 3, 0, 4, 5, 0])
expected_result =  (1, 5)
result = test(arr0)
assert result == expected_result, 'Test failed'