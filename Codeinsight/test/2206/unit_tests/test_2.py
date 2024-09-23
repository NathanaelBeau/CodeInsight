df0 = pd.DataFrame({ 'P': [22, None, 24], 'Q': [None, 23, None], 'R': [None, None, 25] })
lst0 = ['P', 'Q', 'R']
expected_result =  pd.Series([22.0, 23.0, 24.0])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'