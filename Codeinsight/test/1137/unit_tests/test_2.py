data1 = {'date': ['2023-06-01', '2023-06-02', '2023-06-03'],
         'revenue': [800, 1200, 1600]}
df1 = pd.DataFrame(data1)
var0 = 'revenue'
var1 = 'date'
col0 = 'CET'
data2 = {'CET': ['2023-06-01', '2023-06-02', '2023-06-03']}
df2 = pd.DataFrame(data2)
expected_output = pd.DataFrame({ 'CET': ['2023-06-01', '2023-06-02', '2023-06-03'], 'revenue': [800, 1200, 1600] })
test_df = test(df1, df2, col0, var0, var1)
assert test_df .equals(expected_output), 'Test failed'