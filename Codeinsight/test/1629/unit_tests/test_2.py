data0 = np.array([['red', 'blue'], [np.nan, 'green'], ['red', np.nan]], dtype=object)
expected_result =  np.array([['red', 'blue'], ['red', 'green'], ['red', 'blue']], dtype=object)
result = test(data0)
assert (result == expected_result).all(), 'Test failed'