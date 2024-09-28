# Test 3
df0 = pd.DataFrame({'name': ['John', '  ', 'Jane'], 'gender': ['M', '   ', 'F']})
expected_result =  pd.DataFrame({'name': ['John', np.nan, 'Jane'], 'gender': ['M', np.nan, 'F']})
result = test(df0)
assert result.equals(expected_result), 'Test failed'