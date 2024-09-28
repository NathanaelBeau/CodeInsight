# Test 2
df0 = pd.DataFrame({'fruit': ['apple', '  ', 'banana'], 'count': [10, '  ', 20]})
expected_result =  pd.DataFrame({'fruit': ['apple', np.nan, 'banana'], 'count': [10, np.nan, 20]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'