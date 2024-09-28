# Test 2
df0 = pd.DataFrame({ "X": [1, 2, 3], "Y": [4, None, 6] })
expected_result =  True
result = test(df0)
assert result == expected_result, 'Test failed'