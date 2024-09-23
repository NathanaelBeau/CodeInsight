var1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_first = pd.Series({'A': 0, 'B': 0})
expected_last = pd.Series({'A': 2, 'B': 2})
result_first, result_last = test(var1)
assert result_first.equals(expected_first) and result_last.equals(expected_last), 'Test failed'