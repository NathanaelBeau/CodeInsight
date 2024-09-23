df0 = pd.DataFrame({'A': [1, 2]})
df1 = pd.DataFrame({'B': [3, 4]})
expected_result =  pd.DataFrame({'A': [1, 1, 2, 2], 'B': [3, 4, 3, 4]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'