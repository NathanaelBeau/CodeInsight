arr0 = np.array([[0], [1], [2]])
expected_result =  [[0, 1, 2]]
result = test(arr0)
assert result == expected_result, 'Test failed'