df0 = pd.DataFrame({'key': [1, 2, 3], 'A': ['a', 'b', 'c']})
df1 = pd.DataFrame({'key': [1, 2, 3], 'B': ['d', 'e', 'f'], 'A': ['z', 'y', 'x']})
var0 = 'key'
expected_result =  pd.DataFrame({'key': [1, 2, 3], 'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']})
result = test(df0, df1, var0)
assert result.equals(expected_result), 'Test failed'