df0 = pd.DataFrame({'A': [1, 1, 2, 2], 'B': [3, 3, 4, 4], 'C': [5, 5, 6, 6]})
lst0 = ['A', 'C']
expected_result2 = pd.DataFrame({'A': [1, 2], 'C': [5, 6], 'var0': [2, 2]})
result2 = test(df0, lst0)
assert result2.equals(expected_result2), 'Test failed'