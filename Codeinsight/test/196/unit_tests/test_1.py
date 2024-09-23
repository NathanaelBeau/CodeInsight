# Test 2
df0_1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']})
column_name_2 = 'B'
lst0_2 = ['a', 'd']
expected_result_2 = pd.DataFrame({'A': [1, 4], 'B': ['a', 'd']})
result_2 = test(df0_1, column_name_2, lst0_2)
assert result_2.equals(expected_result_2), 'Test failed'