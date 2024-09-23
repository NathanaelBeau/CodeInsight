arr0 = np.array([[11, 22], [33, 44], [55, 66]])
lst0 = []
lst1 = [0]
expected_result =  np.array([[22], [44], [66]])
result = test(arr0, lst0, lst1)
assert np.array_equal(result, expected_result), 'Test failed'