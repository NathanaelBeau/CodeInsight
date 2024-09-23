# Test 3
lists = [['John', 'Jane'], [30, 25], ['M', 'F']]
col_names = ['name', 'age', 'gender']
expected_result =  pd.DataFrame({'name': ['John', 'Jane'], 'age': [30, 25], 'gender': ['M', 'F']})
result = test(lists, col_names)
assert result.equals(expected_result), 'Test failed'