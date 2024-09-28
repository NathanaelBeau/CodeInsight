# Test 1
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6] })
expected_result =  3
assert test(df0) == expected_result, 'Test failed'