df0 = pd.DataFrame({ 'A': [9, 10, 11, 12], 'B': [13, 14, 15, 16] })
expected_result =  df0  # No NaN values
result = test(df0)
assert result.equals(expected_result), 'Test failed'