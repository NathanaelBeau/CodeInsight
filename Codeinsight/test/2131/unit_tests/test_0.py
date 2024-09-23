# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
col_name = 'A'
lst0 = [2, 4]
expected_result =  pd.DataFrame({'A': [2, 4], 'B': [20, 40]})
result = test(df0, col_name, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'