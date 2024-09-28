# Test 3
df0 = pd.DataFrame({'M': [10.5, 11.5]}, index=['a', 'b'])
df1 = pd.DataFrame({'N': [12.5, 13.5]}, index=['b', 'a'])
expected_result =  pd.DataFrame({'M': [10.5, 11.5], 'N': [13.5, 12.5]}, index=['a', 'b'])
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'