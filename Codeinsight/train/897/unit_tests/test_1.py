data = {'A': [np.nan, np.nan, np.nan],
         'B': [1, 2, 3],
         'C': [4, np.nan, 6]}
df0 = pd.DataFrame(data)
expected_output = pd.DataFrame({'B': [1, 2, 3],
                                 'C': [4, np.nan, 6]})
assert test(df0) .equals(expected_output), 'Test failed'