# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana'], 'count': [10, 20], 'color': ['red', 'yellow']})
expected_result =  3
result = test(df0)
assert result == expected_result, 'Test failed'