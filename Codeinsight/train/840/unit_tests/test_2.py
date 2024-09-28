df2 = pd.DataFrame({ 'P': [11, 12, 13, 14], 'Q': [15, 16, 17, 18] })
expected_result =  pd.Series({'P': 4, 'Q': 4})
result = test(df2)
assert result.equals(expected_result), 'Test failed'