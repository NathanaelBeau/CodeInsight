# Test 3
df0 = pd.DataFrame({'Group': ['alpha', 'beta', 'alpha', 'beta'], 'Score': [50, 75, 90, 60]})
var0 = 'Group'
expected_result =  pd.DataFrame({'Score': [140, 135]}, index=['alpha', 'beta'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'