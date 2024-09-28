df0 = pd.DataFrame({'values': [1, 5, 10, 15, 20]})
str0 = 'values'
lst0 = [0, 10, 20]
expected_result =  pd.cut(df0['values'], lst0)
result = test(df0, str0, lst0)
assert result.equals(expected_result), 'Test failed'