# Test 1
df0 = pd.DataFrame({'A': ['apple', 'banana', 'grape']})
value0 = 'banana'
expected_result =  True
result = test(df0, 'A', value0)
assert result == expected_result, 'Test failed'