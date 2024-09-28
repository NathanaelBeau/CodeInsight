ser0 = pd.Series([4, 5, 6], index=pd.MultiIndex.from_tuples([('d', 4), ('e', 5), ('f', 6)]))
expected_result =  pd.Series([4, 5, 6])
result = test(ser0)
assert result.equals(expected_result), 'Test failed'