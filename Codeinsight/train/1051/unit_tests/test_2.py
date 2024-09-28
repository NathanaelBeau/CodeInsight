df0 = pd.DataFrame({ 'X_data': [19, 20, 21], 'Y_data': [22, 23, 24], 'Z_info': [25, 26, 27] })
str0 = 'data'
expected_result =  pd.DataFrame({ 'Z_info': [25, 26, 27] })
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'