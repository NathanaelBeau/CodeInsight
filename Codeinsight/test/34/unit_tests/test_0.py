# Test 1
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
lst0 = [df1, df2]
expected_result =  pd.DataFrame({'A': [1, 2, 3, 7, 8, 9], 'B': [4, 5, 6, 10, 11, 12]})
result = test(lst0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'