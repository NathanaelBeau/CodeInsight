df0 = pd.DataFrame({'Col1': [1, 2, 3], 'Col2': [4, 5, 6]}, index=['Row1', 'Row2', 'Row3'])
expected_output = ['Row1', 'Row2', 'Row3']
assert test(df0) ==expected_output, 'Test failed'