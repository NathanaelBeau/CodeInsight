df1 = pd.DataFrame({ ('P', 'type1'): [7, 8], ('Q', 'type2'): [9, 10] })
new_column_tuple1 = ('R', 'type3')
values_list1 = [11, 12]
expected_result =  pd.DataFrame({ ('P', 'type1'): [7, 8], ('Q', 'type2'): [9, 10], ('R', 'type3'): [11, 12] })
result = test(df1, new_column_tuple1, values_list1)
assert result.equals(expected_result), 'Test failed'