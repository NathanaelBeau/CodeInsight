df2 = pd.DataFrame({'M': [5, 6, 7, 8], 'N': [9, 10, 11, 12]})
colA = 'M'
some_value = 8
colB = 'N'
new_value = 0
expected_result =  pd.DataFrame({'M': [5, 6, 7, 8], 'N': [9, 10, 11, 0]})
result = test(df2, colA, some_value, colB, new_value)
assert result.equals(expected_result), 'Test failed'