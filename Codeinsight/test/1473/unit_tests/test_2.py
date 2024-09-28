lst0 = ['a', 'abc', 'abcdef']
expected_result =  np.array(['a', 'abc', 'abcdef'], dtype=object)
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'