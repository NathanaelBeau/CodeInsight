# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', np.nan], 'age': [30., np.nan, 40.]})
expected_result =  pd.DataFrame({'name': ['John', 'Jane', 'Anonymous'], 'age': [30., 'Anonymous', 40.]})
result = test(df0, ['name', 'age'], 'Anonymous')  # This test is meant to fail, as using a single value for multiple columns is incorrect
assert result.equals(expected_result), 'Test failed'