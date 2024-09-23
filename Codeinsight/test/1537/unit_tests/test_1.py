var0 = 'B'
df0 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [np.nan, np.nan, 3, 4]})
expected_result =  pd.DataFrame({'A': [1, 2], 'B': [np.nan, np.nan]}, index=[0, 1])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'