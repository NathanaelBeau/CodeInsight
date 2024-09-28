# Test 1
df0 = pd.DataFrame({'A': ['apple', 'banana', np.nan, 'grape']})
expected_result =  pd.DataFrame({'A': ['apple', 'banana', 'grape']})
result = test(df0, 'A').reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'