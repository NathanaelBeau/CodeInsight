data0 = [('hello', 10), ('world', 20)]
expected_result =  np.array([('hello', 10), ('world', 20)], dtype=object)
result = test(data0)
assert np.array_equal(result, expected_result), 'Test failed'