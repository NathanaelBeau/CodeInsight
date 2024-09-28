lst0 = [{'a': 1, 'b': {'c': 2}}, {'a': 3, 'b': {'c': 4}}]
expected_result =  pd.DataFrame({'a': [1, 3], 'b.c': [2, 4]})
assert test(lst0).equals(expected_result), 'Test failed'