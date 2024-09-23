# Test 3
df0_1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']})
lst0_3 = [4, 5]
column_name_1 = 'A'
expected_result_3 = pd.DataFrame({'A': [4], 'B': ['d']})
result_3 = test(df0_1, column_name_1, lst0_3)
assert result_3.equals(expected_result_3), 'Test failed'