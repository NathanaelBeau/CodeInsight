df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6]})
lst0 = ['A', 'B']
expected_result =  pd.DataFrame({'C': [5, 6]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'