# Test 2
df0 = pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['d', 'e', 'f'], 'Z': ['g', 'h', 'i']})
lst0 = ['X', 'Z']
expected_result =  pd.DataFrame({'X': ['a', 'b', 'c'], 'Z': ['g', 'h', 'i']})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'