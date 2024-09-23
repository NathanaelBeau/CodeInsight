df0 = pd.DataFrame({'X': [5, 10, 15], 'Y': [10, 20, 30]})
expected_result =  pd.DataFrame({'X': [0.0, 0.5, 1.0], 'Y': [0.0, 0.5, 1.0]})
result = test(df0)
assert result.equals(expected_result), 'Test failed'