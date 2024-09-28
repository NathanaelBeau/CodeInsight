df2 = pd.DataFrame({ ('X', 'catA'): [13, 14], ('Y', 'catB'): [15, 16] })
new_column_tuple2 = ('Z', 'catC')
values_list2 = [17, 18]
expected_result =  pd.DataFrame({ ('X', 'catA'): [13, 14], ('Y', 'catB'): [15, 16], ('Z', 'catC'): [17, 18] })
result = test(df2, new_column_tuple2, values_list2)
assert result.equals(expected_result), 'Test failed'