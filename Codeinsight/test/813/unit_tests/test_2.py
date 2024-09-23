df0 = pd.DataFrame({"A": [13, 14], "B": [15, 16]}, index=[5, 10])
expected_output = [5, 10]
assert test(df0) == expected_output, 'Test failed'