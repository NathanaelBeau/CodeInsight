df0 = pd.DataFrame({'X': ['a'], 'Y': ['b'], 'Z': ['c']})
expected_result =  [['a', 'b', 'c']]
assert test(df0) == expected_result, 'Test failed'