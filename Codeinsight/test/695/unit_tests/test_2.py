# Test 3
df0 = pd.DataFrame({ "P": [None, None, None], "Q": [None, None, None] })
expected_result =  True
result = test(df0)
assert result == expected_result, 'Test failed'