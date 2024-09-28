df0 = pd.DataFrame({'Column1': [1.1, 2.2, 3.3], 'Column2': [4.4, 5.5, 6.6]})
expected_output = ['0', '1', '2']
assert test(df0) ==expected_output, 'Test failed'