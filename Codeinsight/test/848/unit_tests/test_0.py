var0 = 'B'
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  df0.iloc[[2]]
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'