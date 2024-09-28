df0 = pd.DataFrame({ 'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 9], 'C': [10, 11, 12, 13, 14] })
lst0 = [1, 2]
lst1 = ['A', 'B']
expected_result =  pd.Series([2.5, 6.5], index=['A', 'B'])
result = test(df0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'