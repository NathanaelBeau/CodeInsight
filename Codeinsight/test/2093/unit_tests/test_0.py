df2 = pd.DataFrame({'Group': ['A', 'A', 'B', 'B'], 'Value': [1, 2, 2, 3]})
result_2 = test(df2, 'Group', 'Value')
expected_2 = pd.Series([1, 2], index=['A', 'B'], name='Value')
assert result_2.equals(expected_2),  'Test failed'