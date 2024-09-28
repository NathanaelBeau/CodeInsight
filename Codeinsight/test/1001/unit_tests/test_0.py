df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
column = 'C'
value = [7, 8, 9]
expected_output = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
result = test(df0.copy(), column, value)
assert result.equals(expected_output), 'Test failed'