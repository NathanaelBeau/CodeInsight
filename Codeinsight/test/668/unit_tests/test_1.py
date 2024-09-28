var0 = pd.DataFrame({ 'Status': ['Active', None, 'Other', 'Inactive'] })
col0 = 'Status'
expected_result =  pd.DataFrame({ 'Status': [None, 'Other'] }).reset_index(drop=True)
result = test(var0, col0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'