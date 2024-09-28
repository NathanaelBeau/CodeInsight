# Test 2
df0 = pd.DataFrame({'X': ['a', 'b', -np.inf, 'd'], 'Y': ['e', 'f', 'g', 'h']})
var0 = 'X'
expected_result =  pd.DataFrame({'X': ['a', 'b', 'd'], 'Y': ['e', 'f', 'h']})
result = test(df0, var0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'