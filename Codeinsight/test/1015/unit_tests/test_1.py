# Test 2
columns_list = ['X', 'Y']
expected_result =  pd.DataFrame(columns=['X', 'Y'])
result = test(columns_list)
assert result.equals(expected_result), 'Test failed'