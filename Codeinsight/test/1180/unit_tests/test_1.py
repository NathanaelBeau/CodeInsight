df1 = pd.DataFrame({'A': [7, 8, 9]})
df2 = pd.DataFrame({'C': [10, 11, 12]})
expected_result =  pd.DataFrame({'A': [7, 8, 9], 'C': [10, 11, 12]})
result = test(df1, df2)
assert result.equals(expected_result), 'Test failed'