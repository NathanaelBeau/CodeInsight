lst0 = ['a', 'ab', 'abc']
expected_result =  np.array(['a', 'ab', 'abc'], dtype=object)
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'