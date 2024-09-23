# Unit Test 2
df0 = pd.DataFrame({ 'Name': ['John', 'Jane', 'Doe', 'Alice'], 'Age': [25, 26, 27, 28] })
var0 = 'Name'
var1 = 'Jane'
expected_result =  pd.DataFrame({ 'Name': ['John', 'Doe', 'Alice'], 'Age': [25, 27, 28] })
result = test(df0, var0, var1)
assert result.equals(expected_result), 'Test failed'