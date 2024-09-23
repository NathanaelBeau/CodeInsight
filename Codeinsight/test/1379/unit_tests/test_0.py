lst0 = ['apple', 'banana', 'cherry']
expected_result =  np.array(['apple', 'banana', 'cherry'], dtype=object)
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'