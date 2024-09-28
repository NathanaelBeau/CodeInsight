# Test 3
df0 = pd.DataFrame({'C': [10.01, 11.49, 12.99]}, index=[100, 200, 300])
expected_result =  pd.DataFrame({'C': [10.01, 11.49, 12.99]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'