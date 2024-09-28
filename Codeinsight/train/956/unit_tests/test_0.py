# Test 1
df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry']})
col_name = 'A'
substring = 'apple'
expected_result =  pd.DataFrame({'A': ['banana', 'cherry']},index=[1, 2])
result = test(df0, col_name, substring)
assert result.equals(expected_result), 'Test failed'