df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
lst0 = ['B']
expected_result =  pd.DataFrame({'A': [1, 2]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'