df0 = pd.DataFrame({'sex': [0, 0, 1, 1, 1]})
var0 = 'Female'
var1 = 'Male'
var2 = 'sex'
expected_result =  pd.DataFrame({'sex': ['Female', 'Female', 'Male', 'Male', 'Male']})
result = test(df0, var0, var1, var2)
assert result.equals(expected_result), 'Test failed'