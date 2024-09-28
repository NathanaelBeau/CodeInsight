df0 = pd.DataFrame({'X': [7, 7, 8], 'Y': [9, 9, 10]})
expected_result =  2
result = test(df0)
assert result == expected_result, 'Test failed'