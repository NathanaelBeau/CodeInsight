df0 = pd.DataFrame({'A': [1, 2, 2, 3, 3, 3], 'B': [1, 1, 2, 2, 3, 3], 'C': [1, 2, 3, 4, 5, 6]})
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({'A': [1, 2, 2, 3, 3], 'B': [1, 1, 2, 2, 3], 'C': [1, 2, 3, 4, 5]})
assert test(df0, lst0).equals(expected_result), 'Test failed'