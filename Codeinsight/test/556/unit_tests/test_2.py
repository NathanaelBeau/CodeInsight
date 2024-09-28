var0 = pd.DataFrame({ 'P': [11, 12], 'Q': [13, 14], 'R': [15, 16] })
expected_result =  pd.DataFrame({ 0: [11, 13, 15], 1: [12, 14, 16] })
result = test(var0)
assert result.equals(expected_result), 'Test failed'