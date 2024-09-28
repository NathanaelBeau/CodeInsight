# Test 2
df0 = pd.DataFrame({'X': ['a', 'b', 'c', 'd'], 'Y': ['e', 'f', 'g', 'h']})
lst0 = [1, 2]
expected_result =  pd.DataFrame({'X': ['a', 'd'], 'Y': ['e', 'h']})
result = test(df0, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'