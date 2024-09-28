# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', np.nan], 'count': [10, np.nan, 20]})
expected_result =  ['fruit', 'count']
result = test(df0)
assert set(result) == set(expected_result), 'Test failed'