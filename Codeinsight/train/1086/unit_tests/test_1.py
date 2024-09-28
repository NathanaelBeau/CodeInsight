arr0 = np.array([6, 7, 8, 8, 8, 7])
expected_result =  {6: 1, 7: 2, 8: 3}
result = test(arr0)
assert result == expected_result, 'Test failed'