# Test 2
df0 = pd.DataFrame({'Timestamp': ['2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01'], 'Count': [10, 20, 30, 40]})
var0 = 'Timestamp'
date0 = '2022-05-10'
date1 = '2022-07-20'
expected_result =  pd.DataFrame({'Timestamp': ['2022-06-01', '2022-07-01'], 'Count': [20, 30]})
result = test(df0, var0, date0, date1).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'