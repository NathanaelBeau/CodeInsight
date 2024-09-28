df0 = pd.DataFrame({'X': [1], 'Y': [2], 'Z': [3]})
expected_result =  (1, 3)
result = test(df0)
assert result == expected_result, 'Test failed'