df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8]})
lst0 = ['A', 'D']
expected_result =  pd.DataFrame({'B': [3, 4], 'C': [5, 6]})
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'