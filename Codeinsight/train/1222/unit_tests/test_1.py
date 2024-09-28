# Test 2
df0 = pd.DataFrame({ 'Name': ['John', 'Jane', 'Mike'], 'Age': [30, 25, 40] })
var0 = 'Age'
expected_result =  pd.DataFrame({ 'Name': ['Jane', 'John', 'Mike'], 'Age': [25, 30, 40] }, index=[1,0,2])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'