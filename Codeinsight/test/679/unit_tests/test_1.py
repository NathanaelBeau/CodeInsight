# Test 2
df0 = pd.DataFrame({ 'Scores': [90, 85, 90, 78, 78, 78] })
var0 = 'Scores'
expected_result =  pd.Series({78: 3, 90: 2, 85: 1}, name='Scores')
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'