df0 = pd.DataFrame({'W': [9, 10], 'X': [11, 12], 'Y': [13, 14], 'Z': [15, 16]})
start_column0, end_column0 = 'W', 'Y'
expected_result =  pd.DataFrame({'W': [9, 10], 'X': [11, 12], 'Y': [13, 14]})
result = test(df0.copy(), start_column0, end_column0)
assert result.equals(expected_result), 'Test failed'