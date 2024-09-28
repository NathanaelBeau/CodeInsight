# Test 3
df0 = pd.DataFrame({'C': [np.nan, np.nan, np.nan, np.nan]})
expected_result =  pd.DataFrame({'C': []})
result = test(df0, 'C').reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'