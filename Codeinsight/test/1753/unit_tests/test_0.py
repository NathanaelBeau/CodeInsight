df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['x', 'y', 'z'])
lst0 = ['z', 'x', 'y']
expected_result =  pd.DataFrame({'A': [3, 1, 2], 'B': [6, 4, 5]}, index=['z', 'x', 'y'])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'