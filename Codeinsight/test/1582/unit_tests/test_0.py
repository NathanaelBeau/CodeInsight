var0 = pd.DataFrame({'A': [np.nan, 2, 3], 'B': [4, np.nan, np.nan]})
expected_first = pd.Series({'A': 1, 'B': 0})
expected_last = pd.Series({'A': 2, 'B': 0})
result_first, result_last = test(var0)
assert result_first.equals(expected_first) and result_last.equals(expected_last), 'Test failed'