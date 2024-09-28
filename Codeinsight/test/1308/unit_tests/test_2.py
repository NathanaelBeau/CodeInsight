var0 = pd.DataFrame({'A': [True, False, True], 'B': [True, True, False]})
expected_result =  pd.DataFrame({'A': [2, 1], 'B': [2, 1]}, index=[True, False])
result = test(var0)
assert result.equals(expected_result), 'Test failed'