arr0 = np.array([[10, 20], [30, 40]])
expected_result =  [[10, 30], [20, 40]]
result = test(arr0)
assert result == expected_result, 'Test failed'