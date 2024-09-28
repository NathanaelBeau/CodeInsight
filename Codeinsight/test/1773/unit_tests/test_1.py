df0 = pd.DataFrame({"A": [7, 8, 9], "B": [10, 11, 12]}, index=['x', 'y', 'z'])
expected_output = ['x', 'y', 'z']
assert test(df0) == expected_output, 'Test failed'