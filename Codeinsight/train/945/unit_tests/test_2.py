# Test 3
df0 = pd.DataFrame({'C': [10, 20, 20, 30, 30, 30, 40, 40, 40, 40]})
column_name = 'C'
expected_result =  4
result = test(df0, column_name)
assert result == expected_result, 'Test failed'