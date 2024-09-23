df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]})
start_column0, end_column0 = 'A', 'C'
expected_result =  pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
result = test(df0.copy(), start_column0, end_column0)
assert result.equals(expected_result), 'Test failed'