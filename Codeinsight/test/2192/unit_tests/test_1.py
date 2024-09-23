df0 = pd.DataFrame({'col': ['1', '2', '3']})
str0 = 'number_'
expected_result =  pd.DataFrame({'col': ['number_1', 'number_2', 'number_3']})
assert test(df0, 'col', str0).equals(expected_result), 'Test failed'