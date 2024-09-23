var0 = pd.DataFrame({'sex': [0, 1, 0, 1]})
expected_result =  pd.DataFrame({'sex': ['Female', 'Male', 'Female', 'Male']})
result = test(var0)
assert result.equals(expected_result), 'Test failed'