df0 = pd.DataFrame({'sex': [0, 1, 0, 1]})
var0 = 'Female'
var1 = 'Male'
var2 = 'sex'
expected_result =  pd.DataFrame({'sex': ['Female', 'Male', 'Female', 'Male']})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'