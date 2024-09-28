df0 = pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f']})
var0 = 'Y'
expected_result =  pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': [np.nan, 'd', 'e']})
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'