df0 = pd.DataFrame({'X': [0, 0, 0], 'Y': [3, 4, 5]})
expected_result =  pd.DataFrame({'X': [0, 0, 0], 'Y': [1, 1, 1]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'