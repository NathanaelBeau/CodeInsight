# Test 2
df0 = pd.DataFrame({'X': [np.nan, 'banana'], 'Y': ['orange', np.nan]})
expected_result =  df0  # No numeric columns, so the DataFrame remains unchanged
result = test(df0)
assert result.equals(expected_result), 'Test failed'