df0 = pd.DataFrame({'ID': [1, 2, 3], 'ValueA': ['A', 'B', 'C']})
df1 = pd.DataFrame({'ID': [1, 2, 3], 'ValueB': ['X', 'Y', 'Z']})
var0 = 'ID'
expected_result =  pd.DataFrame({'ID': [1, 2, 3], 'ValueA': ['A', 'B', 'C'], 'ValueB': ['X', 'Y', 'Z']})
result = test(df0, df1, var0)
assert result.equals(expected_result), 'Test failed'