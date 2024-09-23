df0 = pd.DataFrame({'A': [1, 2, 3]})
col0 = 'B'
val0 = 5
label_high = 'high'
label_low = 'low'
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': ['low', 'low', 'low']})
result = test(df0, col0, val0, label_high, label_low)
assert result.equals(expected_result), 'Test failed'