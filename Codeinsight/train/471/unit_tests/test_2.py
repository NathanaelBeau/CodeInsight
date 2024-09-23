# Test 3
df0 = pd.DataFrame({'Name': ['Alice', np.nan, 'Charlie'], 'Age': [25, 30, np.nan]})
expected_result =  pd.DataFrame({'Name': ['Alice', '', 'Charlie'], 'Age': [25, 30, ""]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'