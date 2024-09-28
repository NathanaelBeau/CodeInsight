df0 = pd.DataFrame({'A': [5, 6]}, 
                   index=pd.MultiIndex.from_tuples([('c', 30), ('c', 40)], names=['letters', 'numbers']))
expected_result =  [(('c', 30), 5), (('c', 40), 6)]
result = test(df0)
assert result == expected_result, 'Test failed'