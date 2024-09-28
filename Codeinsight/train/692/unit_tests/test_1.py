data1 = {'X': [1, 2, 3], 'Y': [4, 5, 6]}
data2 = {'X': [10, 20, 30], 'Q': [40, 50, 60]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
var0 = 'X'
expected_result =  pd.DataFrame({'df1': [1, 2, 3], 'df2': [10, 20, 30]})
result = test(df1, df2, var0)
assert result.equals(expected_result), 'Test failed'