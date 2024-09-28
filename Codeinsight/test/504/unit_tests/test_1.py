df0 = pd.DataFrame({ 'X': [10, 20, 30], 'Y': [40, 50, 60], 'X_1': [70, 80, 90] })
expected_result =  pd.DataFrame({ 'X': [40, 50, 60], 'Y': [40, 50, 60] })
assert test(df0).equals(expected_result), 'Test failed'