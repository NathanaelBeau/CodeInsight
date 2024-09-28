var0 = pd.DataFrame({'A': [1, 1, 1, 1, 1]})
expected_result =  pd.DataFrame({'A': [1]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'