# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'apple pie', 'cherry']})
col_name = 'fruit'
substring = 'apple'
expected_result =  pd.DataFrame({'fruit': ['banana', 'cherry']}, index=[1, 3])
result = test(df0, col_name, substring)
assert result.equals(expected_result), 'Test failed'