# Test 2
df0 = pd.DataFrame({'X': ['apple', 'banana']}, index=[10, 11])
df1 = pd.DataFrame({'Y': ['orange', 'grape']}, index=[10, 11])
expected_result =  pd.DataFrame({'X': ['apple', 'banana'], 'Y': ['orange', 'grape']}, index=[10, 11])
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'