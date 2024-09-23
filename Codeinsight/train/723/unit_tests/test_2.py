df0 = pd.DataFrame({ 'A': [1, 2, 3, 4, 5], 'B': [5, 6, 7, 8, 9], 'C': [10, 11, 12, 13, 14] })
lst0 = [0, 1]
lst1 = ['A', 'C']
expected_result =  pd.Series([1.5, 10.5], index=['A', 'C'])
result = test(df0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'