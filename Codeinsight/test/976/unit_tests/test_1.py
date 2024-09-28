var0 = pd.Series([10, 11, 12], name='E')
df0 = pd.DataFrame({'A': [13, 14, 15], 'B': [16, 17, 18]})
expected_result =  pd.DataFrame({'E': [10, 11, 12], 'A': [13, 14, 15], 'B': [16, 17, 18]})
result = test(var0, df0)
assert result.equals(expected_result), 'Test failed'