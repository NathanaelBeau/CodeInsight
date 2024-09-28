var0 = pd.DataFrame({'A': [1, 2, 3]})
expected_result =  pd.DataFrame({'A': [1, 2, 3], 'B': [1, 4, 9], 'C': [1, 8, 27]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'