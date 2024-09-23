# Test 2
df0 = pd.DataFrame({ 'X': ['a', 'b', 'c', 'd'], 'Y': ['d', 'e', 'f', 'g'] })
expected_result =  ['X', 'Y']
assert test(df0) == expected_result, 'Test failed'