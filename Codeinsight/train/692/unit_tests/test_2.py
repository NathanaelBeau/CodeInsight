data1 = {'C': ['a', 'b', 'c'], 'D': [1, 2, 3]}
data2 = {'D': [10.0, 20.5, 30.3], 'G': ['x', 'y', 'z']}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
var0 = 'D'
expected_result =  pd.DataFrame({'df1': [1, 2, 3], 'df2': [10.0, 20.5, 30.3]})
result = test(df1, df2, var0)
assert result.equals(expected_result), 'Test failed'