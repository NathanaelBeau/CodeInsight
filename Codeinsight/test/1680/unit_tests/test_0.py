arr0 = np.array([1, 2, 3, 1, 2, 1, 1, 1])
expected_result =  {1: 5, 2: 2, 3: 1}
result = test(arr0)
assert result == expected_result, 'Test failed'