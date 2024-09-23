df0 = pd.DataFrame({'A': [1.5, 2.5, 3.5],
                    'B': [0.5, 1.5, 2.5],
                    'C': [2, 3, 4]})
expected_output = pd.DataFrame({'A': [3.0, 7.5, 14.0],
                               'B': [1.0, 4.5, 10.0]})
assert test(df0) .equals(expected_output), 'Test failed'