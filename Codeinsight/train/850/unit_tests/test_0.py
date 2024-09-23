df1 = pd.DataFrame({ 'names': [['John', 'Doe'], ['Jane', 'Smith'], ['Mike', 'Tyson']] })
col_name1 = 'names'
val1 = 'Jane'
expected_result1 = [False, True, False]
result1 = test(df1, col_name1, val1)
result1_list = result1.tolist()
assert result1_list == expected_result1, 'Test failed'