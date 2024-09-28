var0 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
expected_result =  pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'