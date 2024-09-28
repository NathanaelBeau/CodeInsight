var0 = pd.DataFrame({'A': [1.0, 2.0, 3.0]})
col0 = 'A'
expected_result =  var0.astype(str)
result = test(var0, col0)
assert result.equals(expected_result), 'Test failed'