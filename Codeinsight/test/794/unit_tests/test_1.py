var0 = pd.Series([5.5, 6.1, 7.9])
expected_result =  pd.Series([5, 6, 7])
result = test(var0)
assert result.equals(expected_result), 'Test failed'