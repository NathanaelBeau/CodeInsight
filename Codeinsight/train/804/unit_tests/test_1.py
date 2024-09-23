var0 = pd.DataFrame({'sex': [0, 0, 1, 1, 1]})
expected_result =  pd.DataFrame({'sex': ['Female', 'Female', 'Male', 'Male', 'Male']})
result = test(var0)
assert result.equals(expected_result), 'Test failed'