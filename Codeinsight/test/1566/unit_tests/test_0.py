df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
lst0 = [5, 6]
expected_result =  pd.DataFrame({'A': [1, 2, 5], 'B': [3, 4, 6]})
result = test(df0.copy(), lst0)
assert result.equals(expected_result), 'Test failed'