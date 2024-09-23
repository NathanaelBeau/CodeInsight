arr2 = np.array([-1, -2, -3, -4])
expected_result =  (-1, -4)
result = test(arr2)
assert result == expected_result, 'Test failed'