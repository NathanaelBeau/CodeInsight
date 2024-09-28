df0 = pd.DataFrame({'X': [10, None, 30], 'Y': [None, 200, 300]})
expected_result =  2
assert test(df0) == expected_result, 'Test failed'