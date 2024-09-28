# Test 2
df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
df1 = pd.DataFrame({'X': [10, 30], 'Y': [40, 60]})
expected_result =  pd.DataFrame({'X': [20], 'Y': [50]}, index=[1])
result = test(df0, df1)
assert result.equals(expected_result), 'Test failed'