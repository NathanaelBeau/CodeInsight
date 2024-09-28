df0 = pd.DataFrame({'alpha': [0.1, 0.2, None], 'beta': [0.5, None, None]})
expected_result =  2
assert test(df0) == expected_result, 'Test failed'