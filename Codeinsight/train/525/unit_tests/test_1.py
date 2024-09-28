df0 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 8, 6], 'Z': [5, 8, 12]})
expected_result =  pd.Series(['Y', 'X', 'Z'])
result = test(df0)
assert result.equals(expected_result), 'Test failed'