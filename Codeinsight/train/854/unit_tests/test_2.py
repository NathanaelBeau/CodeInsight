var2 = pd.DataFrame({'A': [np.nan, np.nan, np.nan], 'B': [np.nan, np.nan, np.nan]})
expected_first = pd.Series({'A': None, 'B': None})
expected_last = pd.Series({'A': None, 'B': None})
result_first, result_last = test(var2)
assert result_first.equals(expected_first) and result_last.equals(expected_last), 'Test failed'