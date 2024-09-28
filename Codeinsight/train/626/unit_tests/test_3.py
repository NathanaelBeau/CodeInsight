var0 = pd.DataFrame({'A': [], 'B': []})
expected_result =  pd.DataFrame({'A': [], 'B': []})
result = test(var0)
assert result.equals(expected_result), 'Test failed'