df1 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]})
operation = 'std'
expected_result =  df1.stack().std()
result = test(df1, operation)
assert result == expected_result, 'Test failed'