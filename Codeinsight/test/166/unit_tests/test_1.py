var0 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
expected_result =  pd.DataFrame({'A': [9, 8, 7], 'B': [12, 11, 10]}).reset_index(drop=True)
result = test(var0).reset_index(drop=True)
assert result.equals(expected_result), 'Test failed'