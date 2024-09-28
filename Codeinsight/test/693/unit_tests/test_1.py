df0_1 = pd.DataFrame({'X': [10, 20], 'Y': [30, 40]})
df0_2 = pd.DataFrame({'X': [50, 60]})
df0 = pd.concat([df0_1, df0_2], axis=1)
expected_result =  pd.DataFrame({'X': [60, 80], 'Y': [30, 40]})
assert test(df0).equals(expected_result), 'Test failed'