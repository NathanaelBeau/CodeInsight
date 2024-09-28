# Test 2
df0 = pd.DataFrame({'B': [np.nan, 'orange', 'lemon', np.nan]})
expected_result =  pd.DataFrame({'B': ['orange', 'lemon']})
result = test(df0, 'B').reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'