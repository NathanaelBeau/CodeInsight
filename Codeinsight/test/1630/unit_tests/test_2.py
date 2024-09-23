data = {'A': [1, 2, 3],
         'B': [4, 5, 6]}
df0 = pd.DataFrame(data)
expected_output = pd.DataFrame({'A': [1, 2, 3],
                                 'B': [4, 5, 6]})
assert test(df0) .equals(expected_output), 'Test failed'