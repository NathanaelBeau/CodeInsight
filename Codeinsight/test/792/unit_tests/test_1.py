df0 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]}, index=['u', 'v', 'w'])
lst0 = ['w', 'u', 'v']
expected_result =  pd.DataFrame({'C': [9, 7, 8], 'D': [12, 10, 11]}, index=['w', 'u', 'v'])
result = test(df0, lst0)
assert result.equals(expected_result), 'Test failed'