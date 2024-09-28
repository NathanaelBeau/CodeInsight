# Test 3
df0 = pd.DataFrame({'C': [1.5, 2.5, 3.5, 4.5, 5.5]})
col_name = 'C'
expected_result =  3.5
result = test(df0, col_name)
assert result == expected_result, 'Test failed'