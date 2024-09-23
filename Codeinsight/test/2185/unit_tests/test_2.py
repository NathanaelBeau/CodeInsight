s0 = pd.Series([100, 200, 300], index=['alpha', 'beta', 'gamma'])
s1 = pd.Series([], index=[], dtype='float64')
expected_result =  pd.Series([100, 200, 300], index=['alpha', 'beta', 'gamma'])
assert test(s0, s1).equals(expected_result), 'Test failed'