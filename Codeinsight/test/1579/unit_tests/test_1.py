var0 = pd.DataFrame({'A': ['apple  ', ' banana', ' cherry '], 'B': [' date ', ' fig ', ' grape']})
expected_result2 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': ['date', 'fig', 'grape']})
result2 = test(var0)
assert result2.equals(expected_result2), 'Test failed'