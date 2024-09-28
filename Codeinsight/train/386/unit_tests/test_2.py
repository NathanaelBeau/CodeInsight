df0 = pd.DataFrame({'A': [1, 2, 3]}, index=['a', 'b', 'c'])
df1 = pd.DataFrame({'B': [4, 5]}, index=['a', 'b'])
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, np.nan]}, index=['a', 'b', 'c'])
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'