# Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
dict0 = {'A': 'X', 'B': 'Y'}
expected_result =  pd.DataFrame({ 'X': [1, 2, 3], 'Y': [4, 5, 6] })
assert test(df0.copy(), dict0).equals(expected_result), 'Test failed'