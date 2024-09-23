df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
var0 = ['C', 'A', 'B']
var1 = [2, 0, 1]
expected_output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
result=test(df0, var0, var1)
assert result == expected_output, 'Test failed'