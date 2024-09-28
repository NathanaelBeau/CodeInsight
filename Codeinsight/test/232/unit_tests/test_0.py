# Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3] })
var0 = 'B'
lst0 = [4, 5, 6]
expected_result =  pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
assert test(df0.copy(), var0, lst0).equals(expected_result), 'Test failed'