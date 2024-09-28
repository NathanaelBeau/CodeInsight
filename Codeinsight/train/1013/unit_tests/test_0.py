var0 = 'A'
df0 = pd.DataFrame({'A': [1, 2, np.nan, 4]})
expected_result =  pd.DataFrame({'A': [np.nan]}, index=[2])
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'