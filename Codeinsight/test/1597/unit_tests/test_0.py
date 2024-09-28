df0 = pd.DataFrame({ 'name': [1, 2, 3], 'age_name': [4, 5, 6], 'address': [7, 8, 9] })
str0 = 'name'
expected_result =  pd.DataFrame({ 'address': [7, 8, 9] })
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'