df0 = pd.DataFrame({'A': [10, 20, 30]}, index=['x', 'y', 'z'])
df1 = pd.DataFrame({'B': [40, 50]}, index=['y', 'z'])
expected_result =  pd.DataFrame({'A': [10, 20, 30], 'B': [np.nan, 40, 50]}, index=['x', 'y', 'z'])
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'