arr0 = np.array([7, 9, 11])
arr1 = np.array([8, 10, 12])
expected_result =  np.array([7, 8, 9, 10, 11, 12])
result = test(arr0, arr1)
assert (result  ==  expected_result).all(), 'Test failed'