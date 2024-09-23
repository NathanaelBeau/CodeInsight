df2 = pd.DataFrame({'P': [7, 8, 9], 'Q': [10, 11, 12]})
expected_result =  pd.DataFrame(scaler.fit_transform(df2), columns=df2.columns)
result = test(df2)
assert result.equals(expected_result), 'Test failed'