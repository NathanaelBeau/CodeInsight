var0 = 'C'
df0 = pd.DataFrame({'C': [np.nan, np.nan, np.nan, np.nan]})
expected_result =  df0.copy()
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'