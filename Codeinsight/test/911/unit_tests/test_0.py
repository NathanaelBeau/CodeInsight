df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df1 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
expected_result =  pd.DataFrame({'A': [1, 2, 3, 7, 8, 9], 'B': [4, 5, 6, 10, 11, 12]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'