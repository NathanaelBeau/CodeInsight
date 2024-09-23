# Test 1
columns_list = ['A', 'B', 'C']
expected_result =  pd.DataFrame(columns=['A', 'B', 'C'])
result = test(columns_list)
assert result.equals(expected_result), 'Test failed'