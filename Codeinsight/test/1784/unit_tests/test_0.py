df0 = pd.DataFrame({'A': [1, 2, 'three', 4, 'five'], 'B': [6, 7, 8, 9, 10]})
var0 = 'A'
expected_result =  pd.DataFrame({'A': ['three', 'five'], 'B': [8, 10]}).reset_index(drop=True)
result = test(df0, var0)
assert result.equals(expected_result), 'Test failed'