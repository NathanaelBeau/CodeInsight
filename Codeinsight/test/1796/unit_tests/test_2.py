df0 = pd.DataFrame({'C': [1.1, 2.2, 3.3]}, index=[1, 2, 3])
expected_output = pd.DataFrame({'C': [1.1, 2.2, 3.3]}, index=[1, 2, 3])
assert test(df0).equals(expected_output), 'Test failed'