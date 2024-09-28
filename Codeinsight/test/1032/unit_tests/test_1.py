df0 = pd.DataFrame({ 'X': [None, None, 9], 'Y': [10, None, 12], 'Z': [13, 14, None] })
lst0 = ['X', 'Y', 'Z']
expected_result =  pd.Series([10.0, 14.0, 9.0])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'