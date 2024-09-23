df0 = pd.DataFrame({ 'A': ['a', 'b', 'c', 'd'], 'B': [1, 2, 3, 4] })
lst0 = [1, 3]
expected_result =  pd.DataFrame({ 'A': ['a', 'c'], 'B': [1, 3] }, index=[0, 2])
assert test(df0, lst0).equals(expected_result), 'Test failed'