df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 2], 'C': [7, 8, 9]})
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 2], 'C': [7, 8, 9], 'max_value': [4, 5, 3]})
assert test(df0, lst0).equals(expected_result), 'Test failed'