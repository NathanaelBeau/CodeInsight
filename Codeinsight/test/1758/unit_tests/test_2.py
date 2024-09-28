# Test 3
df0 = pd.DataFrame({'Name': ['Alice'], 'Age': [25], 'Gender': ['Female']})
var0 = 'Gender'
expected_result =  2
result = test(df0, var0)
assert result == expected_result, 'Test failed'