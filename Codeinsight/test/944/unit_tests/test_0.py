# Test 1
df0 = pd.DataFrame({'Date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01'], 'Value': [1, 2, 3, 4]})
var0 = 'Date'
date0 = '2023-01-15'
date1 = '2023-03-15'
expected_result =  pd.DataFrame({'Date': ['2023-02-01', '2023-03-01'], 'Value': [2, 3]})
result = test(df0, var0, date0, date1).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'