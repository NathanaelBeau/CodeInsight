# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4]}, index=[10, 20, 30, 40])
expected_result =  pd.DataFrame({'A': [1, 2, 3, 4]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'