var0 = pd.DataFrame({'A': [1, 2], 'Unnamed: 0': [3, 4]})
expected_result =  pd.DataFrame({'A': [1, 2]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'