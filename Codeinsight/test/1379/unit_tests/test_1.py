lst0 = ['short', 'medium-length-string', 'a-very-long-string-that-goes-on-and-on']
expected_result =  np.array(['short', 'medium-length-string', 'a-very-long-string-that-goes-on-and-on'], dtype=object)
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'