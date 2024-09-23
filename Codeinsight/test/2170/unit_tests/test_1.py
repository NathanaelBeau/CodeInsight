var0 = 1
df0 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
expected_result =  pd.Series([10, 11, 12], name='B')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'