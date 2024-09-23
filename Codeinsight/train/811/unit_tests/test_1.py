var0 = pd.DataFrame({ 'X': [5, 6, 7], 'Y': [8, 9, 10] })
expected_result =  pd.DataFrame({ 0: [5, 8], 1: [6, 9], 2: [7, 10] })
result = test(var0)
assert result.equals(expected_result), 'Test failed'