df1 = pd.DataFrame({ 'X': [7, 7, 7, 7], 'Y': [8, 8, 8, 8], 'Z': [9, 10, 9, 10] })
expected_result =  pd.Series({'X': 1, 'Y': 1, 'Z': 2})
result = test(df1)
assert result.equals(expected_result), 'Test failed'