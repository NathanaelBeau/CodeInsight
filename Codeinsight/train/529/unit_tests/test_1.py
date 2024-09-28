arr0 = np.array([0, 10, 20, 0, 30, 0, 40])
expected_result =  (10, 40)
result = test(arr0)
assert result == expected_result, 'Test failed'