# Test 1
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
lst0 = ['A', 'C']
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'C': [7, 8, 9]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'