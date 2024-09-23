df0 = pd.DataFrame({'A': [1, 2, 2, 3, 3], 'B': [4, 5, 5, 6, 6]})
expected_result =  4
result = test(df0)
assert result == expected_result, 'Test failed'