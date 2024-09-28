df0 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6],
                    'C': [2, 3, 4]})
# Définir la sortie attendue
expected_output = pd.DataFrame({'A': [2, 6, 12],
                               'B': [8, 15, 24]})
assert test(df0) .equals(expected_output), 'Test failed'