df0 = pd.DataFrame({'X': [7, 8, 9], 'Y': [10, 11, 12]}, index=['a', 'b', 'c'])
expected_output = ['a', 'b', 'c']
assert test(df0) == expected_output, 'Test failed'