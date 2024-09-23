df0 = pd.DataFrame({'X': ['a', 'b', 'b', 'c', 'c'], 'Y': ['d', 'd', 'e', 'e', 'f']})
lst0 = ['X']
expected_result =  pd.DataFrame({'X': ['a', 'b', 'c'], 'Y': ['d', 'd', 'e']}, index=[0, 1, 3])
assert test(df0, lst0).equals(expected_result), 'Test failed'