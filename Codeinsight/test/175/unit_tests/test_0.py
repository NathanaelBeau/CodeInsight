df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df1 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
expected_result =  pd.DataFrame({'A': [1, 2, 5, 6], 'B': [3, 4, 7, 8]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'