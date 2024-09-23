# Test 2
df0 = pd.DataFrame({'B': [1, 2, 3, 4]})
value0 = 5
expected_result =  False
result = test(df0, 'B', value0)
assert result == expected_result, 'Test failed'