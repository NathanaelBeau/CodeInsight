var0 = pd.DataFrame({'A': [0, 1, 0], 'B': [0, 0, 2]})
expected_result =  pd.DataFrame({'A': [1, 0], 'B': [0, 2]}, index=[1, 2])
result = test(var0)
assert result.equals(expected_result), 'Test failed'