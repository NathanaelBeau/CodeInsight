df1 = pd.DataFrame({'col1': [[1, 2, 3], [4, 5], [6], [], [7, 8]]})
expected_result1 = pd.Series([3, 2, 1, 0, 2], name='col1')
result1 = test(df1, 'col1')
assert result1.equals(expected_result1), 'Test failed'