# Test 3
df0 = pd.DataFrame({'C': [5.2, 5.1, 5.3, 5.1]})
column_name = 'C'
expected_result =  [5.1, 5.2, 5.3]
result = test(df0, column_name)
assert result == expected_result, 'Test failed'