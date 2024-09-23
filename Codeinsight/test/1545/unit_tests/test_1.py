df2 = pd.DataFrame({'X': [None, None, None, None], 'Y': [10, 20, 30, 40]})
expected_result =  pd.DataFrame({'X': [10, 20, 30, 40], 'Y': [10, 20, 30, 40]})
result = test(df2, 'X', 'Y')
assert result .equals( expected_result), 'Test failed'