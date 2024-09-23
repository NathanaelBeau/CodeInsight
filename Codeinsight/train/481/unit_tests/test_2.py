# Test 3
df0 = pd.DataFrame({'name': ['John', 'Jane', 'Doe'], 'age': [30, 25, 40]})
col_name1 = 'name'
col_name2 = 'age'
expected_result =  {'John': 30, 'Jane': 25, 'Doe': 40}
result = test(df0, col_name1, col_name2)
assert result == expected_result, 'Test failed'