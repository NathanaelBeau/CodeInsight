df0 = pd.DataFrame({'ID': [1, 1, 2, 2], 'Value': [10, 20, 30, 40]})
expected_result =  pd.DataFrame({'ID': [1, 1, 2, 2], 'Value': [10, 20, 30, 40], 'ID_mean': [15.0, 15.0, 35.0, 35.0], 'ID_sum': [30, 30, 70, 70]})
result = test(df0, 'ID', 'Value')
assert result.equals(expected_result), 'Test failed'