df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9] })
expected_result =  pd.Series([7, 8, 9], name='C')
result = test(df0)
assert result.equals(expected_result), 'Test failed'