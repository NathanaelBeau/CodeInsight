var0 = pd.DataFrame({'TEST': [5, 6], 'DATA': [7, 8]})
expected_result =  pd.DataFrame({'test': [5, 6], 'data': [7, 8]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'