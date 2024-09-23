# Test 3
df0 = pd.DataFrame({'A': [1.1, 2.2, 3.3, 4.4, 5.5], 'B': ['a', 'b', 'c', 'd', 'e']})
col_name = 'A'
lst0 = [1.1, 3.3, 5.5]
expected_result =  pd.DataFrame({'A': [1.1, 3.3, 5.5], 'B': ['a', 'c', 'e']})
result = test(df0, col_name, lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'