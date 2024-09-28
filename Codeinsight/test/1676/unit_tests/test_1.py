var0 = pd.DataFrame({'C': [7.0, 8.0, 9.0], 'D': [10.0, 11.0, np.nan]})
expected_result =  pd.DataFrame({'C': [7.0, 8.0, 9.0], 'D': [10.0, 11.0, 0.0]})
result = test(var0)
assert result.equals(expected_result), 'Test failed'