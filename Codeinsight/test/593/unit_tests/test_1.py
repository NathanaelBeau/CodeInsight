df0 = pd.DataFrame({'X': [10, 20, 30, 40], 'Y': [100, 200, 300, 400]})
expected_result =  pd.DataFrame({'X': [10, 20, 30], 'Y': [100, 200, 300]})
assert test(df0).equals(expected_result), 'Test failed'