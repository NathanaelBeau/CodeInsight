# Test 2
lists = [['apple', 'banana'], [10, 20]]
col_names = ['fruit', 'count']
expected_result =  pd.DataFrame({'fruit': ['apple', 'banana'], 'count': [10, 20]})
result = test(lists, col_names)
assert result.equals(expected_result), 'Test failed'