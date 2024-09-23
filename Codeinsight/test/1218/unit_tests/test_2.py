df0 = pd.DataFrame({'alpha': [0.1, 0.2], 'beta': [0.5, 0.6]})
expected_result =  pd.DataFrame({'alpha': [0.1], 'beta': [0.5]})
assert test(df0).equals(expected_result), 'Test failed'