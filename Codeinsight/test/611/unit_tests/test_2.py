df2 = pd.DataFrame({'P': [13, 14], 'Q': [15, 16]})
operation = 'mean'
expected_result =  14.5
result = test(df2, operation)
assert result == expected_result, 'Test failed'