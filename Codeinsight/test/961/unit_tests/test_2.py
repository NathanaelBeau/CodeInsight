# Test 3
df0 = pd.DataFrame({ 'z': ['a', 'b', 'c'], 'x': ['d', 'e', 'f'], 'y': ['g', 'h', 'i'] })
expected_result =  pd.DataFrame({ 'x': ['d', 'e', 'f'], 'y': ['g', 'h', 'i'], 'z': ['a', 'b', 'c'] })
result = test(df0)
assert result.equals(expected_result), 'Test failed'