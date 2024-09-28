arr0 = np.array([1, 3, 5])
arr1 = np.array([2, 4, 6])
expected_result =  np.array([1, 2, 3, 4, 5, 6])
result = test(arr0, arr1)
assert (result  ==  expected_result).all(), 'Test failed'