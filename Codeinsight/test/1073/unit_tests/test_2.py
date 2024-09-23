df0 = pd.DataFrame({'A': [7]}, 
                   index=pd.MultiIndex.from_tuples([('d', 50)], names=['letters', 'numbers']))
expected_result =  [(('d', 50), 7)]
result = test(df0)
assert result == expected_result, 'Test failed'