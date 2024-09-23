# Unit Test 3
df0 = pd.DataFrame({ 'P': [19, 20, 21], 'Q': [22, 23, 24], 'R': [25, 26, 27] })
var0 = 'R'
expected_result =  pd.DataFrame({ 'P': [19, 20, 21], 'Q': [22, 23, 24] })
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'