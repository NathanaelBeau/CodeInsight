arr0 = np.array([4, 4, 4, 5, 5])
expected_result =  {4: 3, 5: 2}
result = test(arr0)
assert result == expected_result, 'Test failed'