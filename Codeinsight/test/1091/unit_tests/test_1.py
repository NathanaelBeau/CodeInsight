var0 = pd.Series([1.2, 2.4, 3.7])
str0 = "ceiling"
expected_result =  pd.Series([2., 3., 4.])
result = test(var0, str0)
assert result.equals(expected_result), 'Test failed'