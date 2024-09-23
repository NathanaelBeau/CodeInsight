var0 = pd.Series([1.2, 2.5, 3.7, 4.0])
expected_result =  pd.Series([1, 2, 3, 4])
result = test(var0)
assert result.equals(expected_result), 'Test failed'