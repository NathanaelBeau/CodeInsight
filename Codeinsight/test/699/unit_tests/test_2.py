df0 = pd.DataFrame({ 'month': ['Jul', 'Aug', 'Sep'], 'value': [70, 80, 90] })
expected_result =  pd.DataFrame({ 'value': [70, 80, 90] }, index=['Jul', 'Aug', 'Sep'])
result = test(df0)
assert result.equals(expected_result), 'Test failed'