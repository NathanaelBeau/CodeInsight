var0 = 0
df0 = pd.DataFrame({'C': ['a', 'b', 'c'], 'D': ['d', 'e', 'f']})
expected_result =  pd.Series(['a', 'b', 'c'], name='C')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'