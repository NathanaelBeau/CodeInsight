df0 = pd.DataFrame({'A': ['a', 'b', 'a', 'a', 'b', 'b'], 'B': ['x', 'x', 'y', 'y', 'x', 'y'], 'C': [1, 2, 3, 4, 5, 6]})
lst0 = ['A', 'B']
expected_result1 = pd.DataFrame({'A': ['a', 'a', 'b', 'b'], 'B': ['x', 'y', 'x', 'y'], 'var0': [1, 2, 2, 1]})
result1 = test(df0, lst0)
assert result1.equals(expected_result1), 'Test failed'