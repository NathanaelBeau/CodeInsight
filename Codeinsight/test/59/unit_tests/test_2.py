df0 = pd.DataFrame({'A': [2, 4, 6],
                    'B': [1, 3, 5],
                    'C': [2, 3, 4]})
expected_output = pd.DataFrame({'A': [4, 12, 24],
                               'B': [2, 9, 20]})
assert test(df0) .equals(expected_output), 'Test failed'