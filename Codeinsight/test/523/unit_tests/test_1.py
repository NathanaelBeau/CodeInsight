# Test 2
df0 = pd.DataFrame({'Type': ['X', 'Y', 'X', 'Y'], 'Count': [5, 10, 15, 20]})
var0 = 'Type'
expected_result =  pd.DataFrame({'Count': [20, 30]}, index=['X', 'Y'])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'