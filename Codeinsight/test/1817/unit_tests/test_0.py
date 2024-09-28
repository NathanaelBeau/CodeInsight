ser0 = pd.Series([1, 2, 3], index=pd.MultiIndex.from_tuples([('a', 1), ('b', 2), ('c', 3)]))
expected_result =  pd.Series([1, 2, 3])
result = test(ser0)
assert result.equals(expected_result), 'Test failed'