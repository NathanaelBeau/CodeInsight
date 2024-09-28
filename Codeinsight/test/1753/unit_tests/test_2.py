df0 = pd.DataFrame({'E': [13, 14, 15], 'F': [16, 17, 18]}, index=['a', 'b', 'c'])
lst0 = ['c', 'a', 'b']
expected_result =  pd.DataFrame({'E': [15, 13, 14], 'F': [18, 16, 17]}, index=['c', 'a', 'b'])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'