df0 = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15]})
lst0 = [0, 3]
lst1 = ['B', 'C']
expected_result =  df0.loc[lst0, lst1].mean()
result = test(df0, lst0, lst1)
assert result.equals(expected_result), 'Test failed'