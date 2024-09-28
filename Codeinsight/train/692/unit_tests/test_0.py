data1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}
data2 = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
var0 = 'A'
expected_result =  pd.DataFrame({'df1': [1, 2, 3], 'df2': [10, 20, 30]})
result = test(df1, df2, var0)
assert result.equals(expected_result), 'Test failed'