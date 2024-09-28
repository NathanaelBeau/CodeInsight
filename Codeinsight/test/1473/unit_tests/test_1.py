# Test 2
lst0 = ['short', 'longer_str', 'medium_len']
expected_result =  np.array(['short', 'longer_str', 'medium_len'], dtype=object)
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'