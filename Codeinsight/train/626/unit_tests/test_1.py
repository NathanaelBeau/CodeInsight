var0 = pd.DataFrame({'A': [9, 7, 8], 'B': [6, 4, 5], 'C': [1, 3, 2]})
expected_result =  pd.DataFrame({'A': [9, 7, 8], 'B': [6, 4, 5], 'C': [1, 3, 2]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'