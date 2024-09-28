df0 = pd.DataFrame({'K': ['a', 'b'], 'L': ['c', 'd'], 'M': ['e', 'f']})
df1 = pd.DataFrame({'K': ['a', 'b'], 'N': ['g', 'h']})
var0 = 'K'
lst0 = ['K', 'L']
expected_result =  pd.DataFrame({'K': ['a', 'b'], 'L': ['c', 'd'], 'N': ['g', 'h']})
result = test(df0, df1, var0, lst0)
assert result.equals(expected_result), 'Test failed'