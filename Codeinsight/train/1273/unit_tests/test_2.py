var0 = 'name'
var1 = 'John'
var2 = 'score'
df0 = pd.DataFrame({'name': ['John', 'Jane', 'Mike'], 'score': [80, 85, 90]})
expected_result =  pd.DataFrame({'name': ['John', 'Jane', 'Mike'], 'score': ['John', 85, 90]})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'