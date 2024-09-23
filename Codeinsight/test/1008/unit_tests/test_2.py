# Test 3
columns_list = ['name', 'age', 'city']
expected_result =  pd.DataFrame(columns=['name', 'age', 'city'])
result = test(columns_list)
assert result.equals(expected_result), 'Test failed'