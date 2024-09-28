df0 = pd.DataFrame({'B': ['a', 'b', 'c', 'd']}, index=['x', 'y', 'y', 'z'])
expected_output = pd.DataFrame({'B': ['a', 'b', 'd']}, index=['x', 'y', 'z'])
assert test(df0).equals(expected_output), 'Test failed'