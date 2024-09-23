# Test 1
df0 = pd.DataFrame({'A': [1, 2, np.nan], 'B': [3, 4, 5], 'C': [np.nan, np.nan, np.nan]})
expected_result =  ['A', 'C']
result = test(df0)
assert set(result) == set(expected_result), 'Test failed'