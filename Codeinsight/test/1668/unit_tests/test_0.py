var0 = 0
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.Series([1, 2, 3], name='A')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'