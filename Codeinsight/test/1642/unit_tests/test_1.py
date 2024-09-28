df0 = pd.DataFrame({'X': [10], 'Y': [20]})
str0 = 'row2'
lst0 = [30, 40]
expected_result =  pd.DataFrame({'X': [10, 30], 'Y': [20, 40]}, index=[0, 'row2'])
result = test(df0.copy(), str0, lst0)
assert result.equals(expected_result), 'Test failed'