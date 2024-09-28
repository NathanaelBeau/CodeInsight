df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
lst0 = ['A', 'B']
expected_output0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'sum': [5, 7, 9]})
assert test(df0, lst0).equals(expected_output0), 'Test failed'