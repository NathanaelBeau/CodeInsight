var0 = pd.DataFrame({'E': [np.nan, np.nan, 15.0], 'F': [16.0, 17.0, 18.0]})
expected_result =  pd.DataFrame({'E': [0.0, 0.0, 15.0], 'F': [16.0, 17.0, 18.0]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'