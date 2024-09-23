# Test 2
df0 = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry'], 'count': [5, 10, 15]})
col_name1 = 'fruit'
col_name2 = 'count'
expected_result =  {'apple': 5, 'banana': 10, 'cherry': 15}
result = test(df0, col_name1, col_name2)
assert result == expected_result, 'Test failed'