df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df1 = pd.DataFrame({'A': [1, 2, 3], 'D': [10, 11, 12]})
var0 = 'A'
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'D': [10, 11, 12]})
result = test(df0, df1, var0, lst0)
assert result.equals(expected_result), 'Test failed'