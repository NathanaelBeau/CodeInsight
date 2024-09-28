# Test 1
df0 = pd.DataFrame({ "A": [1, 2, 3], "B": [4, 5, 6] })
expected_result =  False
result = test(df0)
assert result == expected_result, 'Test failed'