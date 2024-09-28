df0 = pd.DataFrame({'C': [10, 20, 30, 40], 'D': [50, 60, 70, 80]})
var0 = 'C'
lst0 = [10, 40]
expected_result =  pd.DataFrame({'C': [10, 40], 'D': [50, 80]}, index=[0, 3])
result = test(df0, var0, lst0)
assert result.equals(expected_result), 'Test failed'