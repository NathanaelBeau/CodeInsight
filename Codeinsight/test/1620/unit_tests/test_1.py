df0 = pd.DataFrame({ 'Group': ['x', 'y', 'x', 'y'], 'Value': [10, 20, 30, 40], 'Time': pd.to_datetime(['2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04']) })
var0 = 'Group'
var1 = 'Time'
expected_result_2 = df0.loc[[2, 3]].reset_index(drop=True)
result2 = test(df0, var0, var1)
assert (result2.values==expected_result_2.values).all(), 'Test failed'