df0 = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}, index=['a', 'b', 'c', 'd'])
lst0 = ['a', 'c']
expected_result =  pd.DataFrame({'A': [1, 3], 'B': [5, 7]}, index=['a', 'c'])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'