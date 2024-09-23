var0 = pd.DataFrame({'A': ['apple  ', 100, 200], 'B': [' date ', ' fig ', 300]})
expected_result3 = pd.DataFrame({'A': ['apple', 100, 200], 'B': ['date', 'fig', 300]})
result3 = test(var0)
assert result3.equals(expected_result3), 'Test failed'