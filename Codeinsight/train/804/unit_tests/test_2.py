var0 = pd.DataFrame({'sex': [1, 1, 0]})
expected_result =  pd.DataFrame({'sex': ['Male', 'Male', 'Female']})
result = test(var0)
assert result.equals(expected_result), 'Test failed'