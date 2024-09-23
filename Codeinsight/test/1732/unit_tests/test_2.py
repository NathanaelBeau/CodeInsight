# Unit Test 2
df0 = pd.DataFrame({ 'Name': ['John', 'Jane', 'Doe', 'Alice'], 'Age': [25, 26, 27, 28] })
var0 = 'Salary'
expected_result =  False
result = test(df0, var0)
assert result == expected_result, 'Test failed'