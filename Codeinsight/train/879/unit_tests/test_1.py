# Unit Test 2
df0 = pd.DataFrame({'tuple_col': [(7,8), (9,10), (11,12)]})
expected_result =  pd.DataFrame({'col0': [7, 9, 11], 'col1': [8, 10, 12]})
result = test(df0, 'tuple_col')
assert result.equals(expected_result), 'Test failed'