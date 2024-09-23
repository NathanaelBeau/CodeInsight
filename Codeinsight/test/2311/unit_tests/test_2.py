df0 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]}, index=['One', 'Two', 'Three'])
expected_output = ['One', 'Two', 'Three']
assert test(df0) ==expected_output, 'Test failed'