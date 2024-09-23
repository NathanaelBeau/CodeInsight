df0 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]})
col0 = 'A'
value0 = 2
expected_result =  pd.DataFrame({'A': [3, 4], 'B': [7, 8]})
result = test(df0, col0, value0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'