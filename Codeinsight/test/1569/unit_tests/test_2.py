df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
var0 = ['C', 'B', 'A']
var1 = [0, 1, 2]
expected_output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
result=test(df0, var0, var1)
assert result == expected_output, 'Test failed'