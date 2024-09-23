var0 = pd.DataFrame({ 'A': [1, 2], 'B': [3, 4] })
expected_result =  pd.DataFrame({ 0: [1, 3], 1: [2, 4] })
result = test(var0)
assert result.equals(expected_result), 'Test failed'