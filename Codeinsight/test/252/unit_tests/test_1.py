df0 = pd.DataFrame({'X': [1, 2], 'Y': [3, 4], 'Z': [5, 6]})
df1 = pd.DataFrame({'X': [1, 2], 'W': [7, 8]})
var0 = 'X'
lst0 = ['X', 'Y']
expected_result =  pd.DataFrame({'X': [1, 2], 'Y': [3, 4], 'W': [7, 8]})
result = test(df0, df1, var0, lst0)
assert result.equals(expected_result), 'Test failed'