df0 = pd.DataFrame({ 'X': [10, 20, 30], 'Y': [40, 50, 60], 'Z': [70, 80, 90] })
expected_result =  pd.Series([70, 80, 90], name='Z')
result = test(df0)
assert result.equals(expected_result), 'Test failed'