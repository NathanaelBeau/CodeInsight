arr0 = np.array([[8, 9], ["a", 11]])
expected_result =  True
result = test(arr0)
assert result == expected_result, 'Test failed'