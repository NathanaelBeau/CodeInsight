# Test 3
df0 = pd.DataFrame({'Day': ['2023-09-01', '2023-09-15', '2023-09-20', '2023-10-01'], 'Score': [50, 60, 70, 80]})
var0 = 'Day'
date0 = '2023-09-05'
date1 = '2023-09-30'
expected_result =  pd.DataFrame({'Day': ['2023-09-15', '2023-09-20'], 'Score': [60, 70]})
result = test(df0, var0, date0, date1).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'