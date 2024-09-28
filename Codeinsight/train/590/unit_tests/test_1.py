var0 = pd.DataFrame({'A': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [4, 5, 6], 'B': [16, 25, 36], 'C': [64, 125, 216]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'