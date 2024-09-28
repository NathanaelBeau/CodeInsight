# Test 3
df0 = pd.DataFrame({'name': ['John Appleseed', 'Jane', 'Doe', 'Smith', 'Roe']})
col_name = 'name'
substring = 'John'
expected_result =  pd.DataFrame({'name': ['Jane', 'Doe', 'Smith', 'Roe']}, index=[1, 2, 3, 4])
result = test(df0, col_name, substring)
assert result.equals(expected_result), 'Test failed'