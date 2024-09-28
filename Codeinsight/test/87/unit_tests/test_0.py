df0_1 = pd.DataFrame({'A': [1, 2, 3]}, index=['x', 'y', 'z'])
df1_1 = pd.DataFrame({'B': [4, 5, 6]}, index=['x', 'y', 'z'])
expected_result_1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['x', 'y', 'z'])
result_1 = test(df0_1, df1_1)
assert result_1 .equals( expected_result_1), 'Test failed'