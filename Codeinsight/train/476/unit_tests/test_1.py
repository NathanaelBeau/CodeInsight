# Test 2
df0 = pd.DataFrame({'X': ['apple', 'banana'], 'Y': ['orange', 'grape']})
expected_result =  [{'X': 'apple', 'Y': 'orange'}, {'X': 'banana', 'Y': 'grape'}]
result = test(df0)
assert result == expected_result, 'Test failed'