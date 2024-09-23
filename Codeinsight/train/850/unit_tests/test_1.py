df2 = pd.DataFrame({ 'ages': [[25, 30], [35, 40], [45, 50]] })
col_name2 = 'ages'
val2 = 35
expected_result2 = [False, True, False]
result2 = test(df2, col_name2, val2)
result2_list = result2.tolist()
assert result2_list == expected_result2, 'Test failed'