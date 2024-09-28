var0 = 'C'
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 5, 8]})
expected_result =  df0.iloc[[2]]
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'