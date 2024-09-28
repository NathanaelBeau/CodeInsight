# Test 3
df0 = pd.DataFrame({ 'Type': ['x', 'x', 'y', 'y', 'z', 'z'], 'Score': [90, 85, 85, 80, 75, 95] })
var0 = 'Type'
var1 = 'Score'
expected_result =  pd.DataFrame({ 'Type': ['x', 'y', 'z'], 'Score': [90, 85, 95] }, index=[0,2,5])
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'