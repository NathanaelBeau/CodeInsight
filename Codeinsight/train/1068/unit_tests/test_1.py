nvalues = {'Name': ['John', 'Jane', 'Doe'], 'Age': [28, 22, 25]}
expected_output = pd.DataFrame({'Name': ['John', 'Jane', 'Doe'], 'Age': [28, 22, 25]})
assert test(nvalues).equals(expected_output), 'Test failed'