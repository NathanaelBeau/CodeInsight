var0 = pd.DataFrame({'A': ['-', '2', '3'], 'B': ['4', '-', '6']})
expected_result =  pd.DataFrame({'A': ['NaN', '2', '3'], 'B': ['4', 'NaN', '6']})
result = test(var0)
assert result.equals(expected_result), 'Test failed'