var0 = pd.DataFrame({'A': ['-', '-', '-'], 'B': ['-', '-', '-']})
expected_result =  pd.DataFrame({'A': ['NaN', 'NaN', 'NaN'], 'B': ['NaN', 'NaN', 'NaN']})
result = test(var0)
assert result.equals(expected_result), 'Test failed'