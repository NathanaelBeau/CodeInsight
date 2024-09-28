# Test 3
df0 = pd.DataFrame({'C': [10.5, 11.5, 12.5]})
value0 = 10.5
expected_result =  True
result = test(df0, 'C', value0)
assert result == expected_result, 'Test failed'