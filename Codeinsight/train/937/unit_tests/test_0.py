var0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
expected_result1 = pd.DataFrame({'A': [0.25, 0.3333333333333333], 'B': [0.75, 0.6666666666666666]})
result1 = test(var0)
assert result1.equals(expected_result1), 'Test failed'