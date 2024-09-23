var0 = pd.DataFrame({'A': [25, 26, 27, 28, 29, 30], 'B': [31, 32, 33, 34, 35, 36]})
n = 1
expected_result =  var0
result = test(var0, n)
assert result.reset_index(drop=True).equals(expected_result.reset_index(drop=True)), 'Test failed'