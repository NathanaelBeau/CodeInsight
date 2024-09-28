var0 = pd.DataFrame({'A': ['7', '8', '9'], 'B': ['10', '11', '12']})
expected_result =  var0.astype(int)
result = test(var0)
assert result.equals(expected_result), 'Test failed'