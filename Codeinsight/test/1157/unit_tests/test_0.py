df0 = pd.DataFrame({ ('A', 'cat1'): [1, 2], ('B', 'cat2'): [3, 4] })
new_column_tuple0 = ('C', 'cat3')
values_list0 = [5, 6]
expected_result =  pd.DataFrame({ ('A', 'cat1'): [1, 2], ('B', 'cat2'): [3, 4], ('C', 'cat3'): [5, 6] })
result = test(df0, new_column_tuple0, values_list0)
assert result.equals(expected_result), 'Test failed'