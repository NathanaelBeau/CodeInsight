# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
lst0 = ['A', 'B']
new_column_name = 'sum_AB'
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9], 'sum_AB': [5, 7, 9]})
result = test(df0, lst0, new_column_name)
assert result.equals(expected_result), 'Test failed'