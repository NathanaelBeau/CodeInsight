data = {'A': [1, 2, np.nan, 4],
        'B': [np.nan, 2, 3, 4],
        'C': [1, 2, 3, 4]}
df0 = pd.DataFrame(data)
expected_output = pd.DataFrame({'A': [1, 2, np.nan, 4],
        'B': [np.nan, 2, 3, 4],
        'C': [1, 2, 3, 4]})
assert test(df0) .equals(expected_output), 'Test failed'