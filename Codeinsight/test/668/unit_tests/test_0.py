var0 = pd.DataFrame({ 'Name': [None, 'Other', 'John', 'Jane'] })
col0 = 'Name'
expected_result =  pd.DataFrame({ 'Name': [None, 'Other'] })
result = test(var0, col0)
assert result.equals(expected_result), 'Test failed'