var0 = pd.DataFrame({'A': ['1', '2', '3'], 'B': ['4', '5', '6']})
expected_result =  var0.astype(int)
result = test(var0)
assert result.equals(expected_result), 'Test failed'