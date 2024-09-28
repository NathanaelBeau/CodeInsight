df0 = pd.DataFrame({'A': [-1, 0, 1], 'B': [-2, 0, 2]})
expected_result =  pd.DataFrame(StandardScaler().fit_transform(df0), columns=df0.columns)
result = test(df0)
assert result.equals(expected_result), 'Test failed'