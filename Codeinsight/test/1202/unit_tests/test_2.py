df0 = pd.DataFrame({'A': [9, 10]})
df1 = pd.DataFrame({'B': [11, 12]})
expected_result =  pd.DataFrame({'A': [9, 9, 10, 10], 'B': [11, 12, 11, 12]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'