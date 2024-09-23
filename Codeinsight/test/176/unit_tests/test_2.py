# Test 3
df0 = pd.DataFrame({'M': [10, 11], 'N': [12, 13]})
var0 = 2
var1 = 'O'
var2 = [14, 15]
expected_result =  pd.DataFrame({'M': [10, 11], 'N': [12, 13], 'O': [14, 15]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'