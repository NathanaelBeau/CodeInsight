ndarr0 = np.array([1, 2, 3, 2, 5, 2])
item0 = 2
expected_result =  3
result = test(ndarr0, item0)
assert result == expected_result, 'Test failed'