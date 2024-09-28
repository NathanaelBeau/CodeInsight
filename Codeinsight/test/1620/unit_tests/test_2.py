df0 = pd.DataFrame({ 'ID': [1, 2, 1, 2], 'Score': [90, 80, 85, 95], 'Date': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01']) })
var0 = 'ID'
var1 = 'Date'
expected_result_3 = df0.loc[[2, 3]].reset_index(drop=True)
result3 = test(df0, var0, var1)
assert (result3.values==expected_result_3.values).all(), 'Test failed'