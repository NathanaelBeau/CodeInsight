# Note: Since scaling involves floating point operations, there might be slight variations in the results.
# We'll test for approximate equality.
# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({'A': [-1.22474487, 0., 1.22474487], 'B': [-1.22474487, 0., 1.22474487]})
result = test(df0, lst0)
assert result.applymap(lambda x: round(x, 6)).equals(expected_result.applymap(lambda x: round(x, 6))), 'Test failed'