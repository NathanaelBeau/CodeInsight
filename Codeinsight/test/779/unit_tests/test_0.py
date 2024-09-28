df0 = pd.DataFrame({'A': [1, 2, 3, 4]}, index=[1, 2, 2, 3])
expected_output = pd.DataFrame({'A': [1, 2, 4]}, index=[1, 2, 3])
assert test(df0).equals(expected_output), 'Test failed'