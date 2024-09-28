df0 = pd.DataFrame({ 'X': ['w', 'x', 'y', 'z'], 'Y': [10, 20, 30, 40] })
lst0 = [0, 2]
expected_result =  pd.DataFrame({ 'X': ['x', 'z'], 'Y': [20, 40] }, index=[1, 3])
assert test(df0, lst0).equals(expected_result), 'Test failed'