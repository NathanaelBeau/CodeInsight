# Test 1
df0_1 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'c', 'd']})
column_name_1 = 'A'
lst0_1 = [2, 3]
expected_result_1 = pd.DataFrame({'A': [2, 3], 'B': ['b', 'c']})
result_1 = test(df0_1, column_name_1, lst0_1)
assert result_1.equals(expected_result_1), 'Test failed'