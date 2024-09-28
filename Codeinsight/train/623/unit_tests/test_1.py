arr0 = np.array(['a', 'b', 'c'])
expected_output = [{'a': 'a'}, {'a': 'b'}, {'a': 'c'}]
assert test(arr0) == expected_output, 'Test failed'