var0 = pd.DataFrame({ 'Age': [25, 30, 35, None] })
col0 = 'Age'
expected_result =  pd.DataFrame({ 'Age': [float('nan')] }).reset_index(drop=True)
result = test(var0, col0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'