arr0 = np.array([0.5, 1.5, 2.5])
expected_result =  "0.5, 1.5, 2.5"
result = test(arr0)
assert result == expected_result, 'Test failed'