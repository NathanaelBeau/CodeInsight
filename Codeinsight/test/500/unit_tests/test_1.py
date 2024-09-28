df0 = pd.DataFrame({'A': [None, None, None],
                    'B': [None, None, None],
                    'C': [None, None, None]})
expected_output = 9
assert test(df0) ==expected_output, 'Test failed'