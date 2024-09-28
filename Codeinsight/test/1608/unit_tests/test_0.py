var0 = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7], 'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g']})
lst0 = [3, 6]
expected_result1 = pd.DataFrame({'A': [3, 6], 'B': ['c', 'f']}).reset_index(drop=True)
result1 = test(var0, lst0).reset_index(drop=True)
assert result1.equals(expected_result1), 'Test failed'