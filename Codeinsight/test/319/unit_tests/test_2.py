var0 = pd.DataFrame({'A': [4, 4, 5], 'B': ['d', 'd', 'e']})
col0 = 'A'
expected_result =  pd.Series({4: 2, 5: 1})
result = test(var0, col0)
assert result.equals(expected_result), 'Test failed'