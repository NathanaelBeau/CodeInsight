df1 = pd.DataFrame({'Name': ['A', 'B'], 'Value1': [1, 4], 'Value2': [2, 5]})
expected_result1 = pd.DataFrame({'A': [1, 2], 'B': [4, 5]}, index=['Value1', 'Value2'])
result1 = test(df1, 'Name')
assert result1.equals(expected_result1), 'Test failed'