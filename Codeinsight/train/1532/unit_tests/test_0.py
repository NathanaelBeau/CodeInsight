var0 = pd.DataFrame({'A': [1, 2, 2, 3, 4, 4, 4, 5]})
expected_result =  pd.DataFrame({'A': [1, 2, 3, 4, 5]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'