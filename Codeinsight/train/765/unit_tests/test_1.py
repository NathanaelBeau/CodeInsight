ser0 = pd.Series([7, 8, 9], index=pd.MultiIndex.from_tuples([('g', 7), ('h', 8), ('i', 9)]))
expected_result =  pd.Series([7, 8, 9])
result = test(ser0)
assert result.equals(expected_result), 'Test failed'