df0 = pd.DataFrame({'A': [1, 2, 3, 4]}, 
                   index=pd.MultiIndex.from_tuples([('a', 10), ('a', 20), ('b', 10), ('b', 20)], names=['letters', 'numbers']))
expected_result =  [(('a', 10), 1), (('a', 20), 2), (('b', 10), 3), (('b', 20), 4)]
result = test(df0)
assert result == expected_result, 'Test failed'