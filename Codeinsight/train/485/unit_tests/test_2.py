# Test 3
df0 = pd.DataFrame({'M': [0, 0], 'N': [0, 0]})
lst0 = ['M', 'N']
new_column_name = 'sum_MN'
expected_result =  pd.DataFrame({'M': [0, 0], 'N': [0, 0], 'sum_MN': [0, 0]})
result = test(df0, lst0, new_column_name)
assert result.equals(expected_result), 'Test failed'