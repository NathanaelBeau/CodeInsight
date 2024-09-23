df0 = pd.DataFrame({'A': ['apple', 'banana', 'cherry'], 'B': [5, 3, 7]})
lst0 = [3, 5, 7]
var0 = 'B'
expected_result_3 = pd.DataFrame({'A': ['banana', 'apple', 'cherry'], 'B': [3, 5, 7]}).reset_index(drop=True)
result_3 = test(df0, lst0, var0).reset_index(drop=True)
assert result_3.equals(expected_result_3), 'Test failed'