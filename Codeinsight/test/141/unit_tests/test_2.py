# Test 3
df0 = pd.DataFrame({'C': ['123Z', '456Z', '789Z']})
column_name = 'C'
unwanted_string = 'Z'
expected_result =  pd.DataFrame({'C': ['123', '456', '789']})
result = test(df0, column_name, unwanted_string)
assert result.equals(expected_result), 'Test failed'