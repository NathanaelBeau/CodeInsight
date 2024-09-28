var0 = pd.DataFrame({'A': [np.nan, 2.0, 3.0], 'B': [4.0, np.nan, 6.0]})
expected_result =  pd.DataFrame({'A': [0.0, 2.0, 3.0], 'B': [4.0, 0.0, 6.0]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'