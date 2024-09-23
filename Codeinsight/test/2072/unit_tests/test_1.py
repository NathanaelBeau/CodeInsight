df0 = pd.DataFrame({'X': [7, 8, 9, 10], 'Y': [11, 12, 13, 14]})
expected_result =  pd.DataFrame({'X': [7, 10], 'Y': [11, 14]}, index=[0, 3])
result = test(df0)
assert result.equals(expected_result), 'Test failed'