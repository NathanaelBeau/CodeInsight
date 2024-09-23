data0 = np.array([['apple', 'banana'], ['apple', np.nan], [np.nan, 'banana']], dtype=object)
expected_result =  np.array([['apple', 'banana'], ['apple', 'banana'], ['apple', 'banana']], dtype=object)
result = test(data0)
assert (result == expected_result).all(), 'Test failed'