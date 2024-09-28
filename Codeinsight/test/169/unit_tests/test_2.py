var0 = pd.DataFrame({'Name': ['John', 'Jane', 'Mike'], 'Age': [30, 25, 40]})
expected_result =  var0['Name']
result = test(var0)
assert result.equals(expected_result), 'Test failed'