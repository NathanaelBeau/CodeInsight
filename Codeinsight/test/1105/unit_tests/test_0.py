# Unit Test 1
df0 = pd.DataFrame({'tuple_col': [(1,2), (3,4), (5,6)]})
expected_result =  pd.DataFrame({'col0': [1, 3, 5], 'col1': [2, 4, 6]})
result = test(df0, 'tuple_col')
assert result.equals(expected_result), 'Test failed'