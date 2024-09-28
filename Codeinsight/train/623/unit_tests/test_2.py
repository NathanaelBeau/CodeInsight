arr0 = np.array(['1', '2', '3'])
expected_output = [{'1': '1'}, {'1': '2'}, {'1': '3'}]
assert test(arr0) == expected_output, 'Test failed'