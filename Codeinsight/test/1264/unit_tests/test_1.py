arr0 = np.array([1, 2, np.nan, 4, 5])
expected_result =  4
result = test(arr0)
assert result == expected_result, 'Test failed'