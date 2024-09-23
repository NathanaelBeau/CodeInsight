df0 = pd.DataFrame({ 'A': [1, 2, 2, 3], 'B': [3, 4, 4, 5], 'C': [5, 6, 6, 7] })
lst0 = ['A', 'B']
expected_result =  [1, 2, 3, 4, 5]
result = test(df0, lst0)
assert result == expected_result, 'Test failed'