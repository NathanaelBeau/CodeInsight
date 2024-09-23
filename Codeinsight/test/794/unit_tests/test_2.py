var0 = pd.Series([8.0, 9.3])
expected_result =  pd.Series([8, 9])
result = test(var0)
assert result.equals(expected_result), 'Test failed'