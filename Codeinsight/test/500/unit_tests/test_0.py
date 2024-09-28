df0 = pd.DataFrame({'A': [1, 2, None, 4],
                    'B': [5, None, 7, 8],
                    'C': [None, 10, 11, 12]})
expected_output = 3
assert test(df0) ==expected_output, 'Test failed'