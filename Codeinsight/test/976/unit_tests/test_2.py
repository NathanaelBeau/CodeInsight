var0 = pd.Series([19, 20, 21], name='F')
df0 = pd.DataFrame({'G': [22, 23, 24], 'H': [25, 26, 27]})
expected_result =  pd.DataFrame({'F': [19, 20, 21], 'G': [22, 23, 24], 'H': [25, 26, 27]})
result = test(var0, df0)
assert result.equals(expected_result), 'Test failed'