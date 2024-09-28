df0_3 = pd.DataFrame({'A': [1, 2, 3, 4]}, index=['w', 'x', 'y', 'z'])
df1_3 = pd.DataFrame({'B': [4, 5, 6]}, index=['x', 'y', 'z'])
expected_result_3 = pd.DataFrame({'A': [2, 3, 4], 'B': [4, 5, 6]}, index=['x', 'y', 'z'])
result_3 = test(df0_3, df1_3)
assert result_3 .equals( expected_result_3), 'Test failed'