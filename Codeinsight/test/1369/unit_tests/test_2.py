# Test 3
df0 = pd.DataFrame({'M': [0, 0, 0], 'N': [1, 2, 3]})
lst0 = ['M', 'N']
expected_result =  pd.DataFrame({'M': [0., 0., 0.], 'N': [-1.22474487, 0., 1.22474487]})
result = test(df0, lst0)
assert result.applymap(lambda x: round(x, 6)).equals(expected_result.applymap(lambda x: round(x, 6))), 'Test failed'