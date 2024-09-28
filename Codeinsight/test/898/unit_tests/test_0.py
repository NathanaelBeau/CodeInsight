data0 = np.array([['cat', 'dog'], [np.nan, 'dog'], ['cat', np.nan]], dtype=object)
expected_result =  np.array([['cat', 'dog'], ['cat', 'dog'], ['cat', 'dog']], dtype=object)
result = test(data0)
assert (result == expected_result).all(), 'Test failed'