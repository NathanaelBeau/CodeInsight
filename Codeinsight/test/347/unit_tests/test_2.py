data0 = [('cat', 5.5), ('dog', 6.6)]
expected_result =  np.array([('cat', 5.5), ('dog', 6.6)], dtype=object)
result = test(data0)
assert np.array_equal(result, expected_result), 'Test failed'