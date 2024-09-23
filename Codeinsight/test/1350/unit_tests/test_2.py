df0 = pd.DataFrame({'scores': [50, 60, 70, 80, 90]})
str0 = 'scores'
lst0 = [0, 60, 100]
expected_result =  pd.cut(df0['scores'], lst0)
result = test(df0, str0, lst0)
assert result.equals(expected_result), 'Test failed'