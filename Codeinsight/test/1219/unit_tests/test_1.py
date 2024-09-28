var0 = pd.DataFrame({'B': [5, 6], 'Unnamed: 1': [7, 8], 'Unnamed: 2': [9, 10]})
expected_result =  pd.DataFrame({'B': [5, 6]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'