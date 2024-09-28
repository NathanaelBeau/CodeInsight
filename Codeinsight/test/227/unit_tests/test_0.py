var0 = pd.DataFrame({'A': [' 1 ', ' 2 ', ' 3 '], 'B': [' 4 ', ' 5 ', ' 6 ']})
expected_result1 = pd.DataFrame({'A': ['1', '2', '3'], 'B': ['4', '5', '6']})
result1 = test(var0)
assert result1.equals(expected_result1), 'Test failed'