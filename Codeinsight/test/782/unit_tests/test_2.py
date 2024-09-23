df3 = pd.DataFrame({'col3': [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]})
expected_result3 = pd.Series([1, 2, 3, 4], name='col3')
result3 = test(df3, 'col3')
assert result3.equals(expected_result3), 'Test failed'