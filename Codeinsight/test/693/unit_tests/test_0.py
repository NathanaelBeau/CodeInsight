df0_1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df0_2 = pd.DataFrame({'A': [5, 6]})
df0 = pd.concat([df0_1, df0_2], axis=1)
expected_result =  pd.DataFrame({'A': [6, 8], 'B': [3, 4]})
assert test(df0).equals(expected_result), 'Test failed'