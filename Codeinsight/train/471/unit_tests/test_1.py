# Test 2
df0 = pd.DataFrame({'X': ['apple', np.nan, 'banana'], 'Y': [np.nan, 'grape', 'mango']})
expected_result =  pd.DataFrame({'X': ['apple', '', 'banana'], 'Y': ['', 'grape', 'mango']})
result = test(df0)
assert result.equals(expected_result), 'Test failed'