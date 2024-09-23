df3 = pd.DataFrame({ 'grades': [['A', 'B'], ['C', 'D'], ['E', 'F']] })
col_name3 = 'grades'
val3 = 'D'
expected_result3 = [False, True, False]
result3 = test(df3, col_name3, val3)
result3_list = result3.tolist()
assert result3_list == expected_result3, 'Test failed'