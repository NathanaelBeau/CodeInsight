df1 = pd.DataFrame({'X': [0, 0, 0], 'Y': [1, 2, 3]})
expected_result =  pd.DataFrame(scaler.fit_transform(df1), columns=df1.columns)
result = test(df1)
assert result.equals(expected_result), 'Test failed'