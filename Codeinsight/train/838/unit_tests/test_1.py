df0 = pd.DataFrame({ 'A': [10., 20., 30.], 'B': [40., 50., 60.], 'C': [2., 5., 3.] })
columns_list0 = ['A', 'B']
column_name0 = 'C'
expected_result =  pd.DataFrame({ 'A': [5., 4., 10.], 'B': [20., 10., 20.], 'C': [2., 5., 3.] })
result = test(df0.copy(), columns_list0, column_name0)
assert result.equals(expected_result), 'Test failed'