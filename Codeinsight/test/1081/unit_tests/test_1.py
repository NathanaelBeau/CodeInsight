df0 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
expected_result =  pd.DataFrame(StandardScaler().fit_transform(df0), columns=df0.columns)
result = test(df0)
assert result.equals(expected_result), 'Test failed'