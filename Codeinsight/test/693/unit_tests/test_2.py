df0_1 = pd.DataFrame({'alpha': [100, 200], 'beta': [300, 400]})
df0_2 = pd.DataFrame({'alpha': [500, 600]})
df0 = pd.concat([df0_1, df0_2], axis=1)
expected_result =  pd.DataFrame({'alpha': [600, 800], 'beta': [300, 400]})
assert test(df0).equals(expected_result), 'Test failed'