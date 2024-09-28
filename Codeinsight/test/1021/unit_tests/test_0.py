var0 = pd.DataFrame({' A ': [1, 2], ' B ': [3, 4], ' C ': [5, 6]})
expected_result =  pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'