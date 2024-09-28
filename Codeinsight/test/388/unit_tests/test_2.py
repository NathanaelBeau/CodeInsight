df0 = pd.DataFrame({'ID': [5, 5, 6, 6], 'Value': [1000, 2000, 3000, 4000]})
expected_result =  pd.DataFrame({'ID': [5, 5, 6, 6], 'Value': [1000, 2000, 3000, 4000], 'ID_mean': [1500.0, 1500.0, 3500.0, 3500.0], 'ID_sum': [3000, 3000, 7000, 7000]})
result = test(df0, 'ID', 'Value')
assert result.equals(expected_result), 'Test failed'