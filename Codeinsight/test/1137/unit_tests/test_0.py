df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [1, 2, 3]})
df3 = pd.DataFrame({'A': [7, 8, 9], 'B': [7, 8, 9]})
lst0 = [df1, df2, df3]
expected_result =  pd.DataFrame({'A': [4.0, 5.0, 6.0], 'B': [4.0, 5.0, 6.0]})
result = test(lst0)
assert result.equals(expected_result), 'Test failed'