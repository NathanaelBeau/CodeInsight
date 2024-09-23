s0 = pd.Series([], index=[], dtype='float64')
s1 = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
expected_result =  pd.Series([10, 20, 30], index=['x', 'y', 'z'])
assert test(s0, s1).equals(expected_result), 'Test failed'