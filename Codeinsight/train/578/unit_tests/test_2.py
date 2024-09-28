df0 = pd.DataFrame({ 'col1': [10, 20, 30], 'col2': [40, 50, 60], 'col3': [70, 80, 90] })
var0 = 'col1'
expected_result =  pd.DataFrame({ 'col2': [40, 50, 60], 'col3': [70, 80, 90] })
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'