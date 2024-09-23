df0 = pd.DataFrame({'ID': [3, 3, 4, 4], 'Value': [100, 200, 300, 400]})
expected_result =  pd.DataFrame({'ID': [3, 3, 4, 4], 'Value': [100, 200, 300, 400], 'ID_mean': [150.0, 150.0, 350.0, 350.0], 'ID_sum': [300, 300, 700, 700]})
result = test(df0, 'ID', 'Value')
assert result.equals(expected_result), 'Test failed'