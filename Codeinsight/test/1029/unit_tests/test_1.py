df0 = pd.DataFrame({'x': [7, 8], 'y': [10, 9]})
df1 = pd.DataFrame({'x': [11, 12], 'y': [8, 7]})
expected_result =  pd.DataFrame({'x': [12, 11, 8, 7], 'y': [7, 8, 9, 10]})
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'