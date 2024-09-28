data0 = [('apple', 1, 1.5), ('banana', 2, 2.5)]
expected_result =  np.array([('apple', 1, 1.5), ('banana', 2, 2.5)], dtype=object)
result = test(data0)
assert np.array_equal(result, expected_result), 'Test failed'