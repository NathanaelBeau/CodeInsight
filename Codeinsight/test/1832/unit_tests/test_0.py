df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
scaler = StandardScaler()
expected_result =  pd.DataFrame(scaler.fit_transform(df0), columns=df0.columns)
result = test(df0)
assert result.equals(expected_result), 'Test failed'