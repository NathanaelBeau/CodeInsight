var0 = pd.DataFrame({'Name': ['John', 'Jane', 'John', 'Jane'], 'Value': [10, 20, 30, 40]})
col0 = 'Name'
col1 = 'Value'
expected_result =  pd.DataFrame({'Name': ['Jane', 'John'], 'Value': [60, 40]})
result = test(var0, col0, col1)
assert result.equals(expected_result), 'Test failed'