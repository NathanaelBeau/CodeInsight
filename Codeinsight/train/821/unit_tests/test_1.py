df0 = pd.DataFrame({'id': [4, 5, 6], 'X': ['m', 'n', 'o']})
df1 = pd.DataFrame({'id': [4, 5, 6], 'Y': ['p', 'q', 'r'], 'X': ['s', 't', 'u']})
var0 = 'id'
expected_result =  pd.DataFrame({'id': [4, 5, 6], 'X': ['m', 'n', 'o'], 'Y': ['p', 'q', 'r']})
result = test(df0, df1, var0)
assert result.equals(expected_result), 'Test failed'