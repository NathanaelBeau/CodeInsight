# Test 2
df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [30, 40, 50], 'Z': [50, 60, 70]})
lst0 = ['X', 'Y']
expected_result =  pd.DataFrame({'X': [-1.22474487, 0., 1.22474487], 'Y': [-1.22474487, 0., 1.22474487], 'Z': [50, 60, 70]})
result = test(df0, lst0)
assert result.applymap(lambda x: round(x, 6)).equals(expected_result.applymap(lambda x: round(x, 6))), 'Test failed'