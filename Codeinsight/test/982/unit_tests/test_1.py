df0 = pd.DataFrame({ 'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 9], 'C': [10, 11, 12, 13, 14] })
lst0 = [2, 3, 4]
lst1 = ['B', 'C']
expected_result =  pd.Series([8.0, 13.0], index=['B', 'C'])
result = test(df0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'