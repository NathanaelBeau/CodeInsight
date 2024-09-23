df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60]})
expected_result =  [10, 40, 20, 50, 30, 60]
result = test(df0)
assert result == expected_result, 'Test failed'