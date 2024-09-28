df0 = pd.DataFrame({'A': [1, 2, 3, 4],
                    'B': [5, 6, 7, 8],
                    'C': [9, 10, 11, 12]})
expected_output = 0
assert test(df0) ==expected_output, 'Test failed'