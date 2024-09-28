# Unit Test 3
df0 = pd.DataFrame({ 'X': [], 'Y': [] })
expected_result =  True
result = test(df0)
assert result == expected_result, 'Test failed'