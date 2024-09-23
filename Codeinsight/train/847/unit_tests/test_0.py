df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
lst0 = [df1, df2]
expected_result =  pd.DataFrame({'A': [1, 2, 5, 6], 'B': [3, 4, 7, 8]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'