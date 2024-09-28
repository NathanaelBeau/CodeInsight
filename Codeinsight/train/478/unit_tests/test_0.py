var0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
expected_result =  pd.DataFrame({'A': [3, 2, 1], 'B': [6, 5, 4]}).reset_index(drop=True)
result = test(var0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'