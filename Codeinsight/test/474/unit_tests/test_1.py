var0 = pd.DataFrame({'ID': [1, 2, 1, 2], 'Scores': [100, 200, 300, 400]})
col0 = 'ID'
col1 = 'Scores'
expected_result =  pd.DataFrame({'ID': [1, 2], 'Scores': [400, 600]})
result = test(var0, col0, col1)
assert result.equals(expected_result), 'Test failed'