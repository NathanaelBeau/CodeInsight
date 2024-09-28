df1 = pd.DataFrame({'A': [1, 2, 3]})
df2 = pd.DataFrame({'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
result = test(df1, df2)
assert result.equals(expected_result), 'Test failed'