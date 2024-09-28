ndarr0 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
item0 = 4
expected_result =  1
result = test(ndarr0, item0)
assert result == expected_result, 'Test failed'