# Test 2
df0 = pd.DataFrame({ 'Name': ['John', 'John', 'Jane', 'Jane'], 'Scores': [90, 85, 88, 78] })
var0 = 'Name'
var1 = 'Scores'
expected_result =  pd.Series({ 'John': [90, 85], 'Jane': [88, 78] }, name='Scores')
result = test(df0, var0, var1)
assert result.sort_index().equals(expected_result.sort_index()), 'Test failed'