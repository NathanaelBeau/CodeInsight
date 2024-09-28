var0 = pd.DataFrame({'A': [3, 3, 3, 6, 6], 'B': ['p', 'q', 'r', 's', 't']})
lst0 = [3, 6]
expected_result3 = pd.DataFrame({'A': [3, 3, 3, 6, 6], 'B': ['p', 'q', 'r', 's', 't']})
result3 = test(var0, lst0)
assert result3.equals(expected_result3), 'Test failed'