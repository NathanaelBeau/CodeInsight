# Test 2
df0 = pd.DataFrame({'B': ['a', 'b', 'c']}, index=[5, 6, 7])
expected_result =  pd.DataFrame({'B': ['a', 'b', 'c']})
result = test(df0)
assert result.equals(expected_result), 'Test failed'