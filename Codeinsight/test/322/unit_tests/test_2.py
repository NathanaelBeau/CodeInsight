df2 = pd.DataFrame({ 'P': [1, 2, 3, 4], 'Q': [1, 2, 3, 4] })
expected_result =  pd.Series({'P': 0.0, 'Q': 0.0})
result = test(df2)
assert result.equals(expected_result), 'Test failed'