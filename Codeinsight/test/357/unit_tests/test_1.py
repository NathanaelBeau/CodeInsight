df0_2 = pd.DataFrame({'A': [1, 2]}, index=['x', 'y'])
df1_2 = pd.DataFrame({'B': [4, 5, 6]}, index=['x', 'y', 'z'])
expected_result_2 = pd.DataFrame({'A': [1, 2], 'B': [4, 5]}, index=['x', 'y'])
result_2 = test(df0_2, df1_2)
assert result_2 .equals( expected_result_2), 'Test failed'