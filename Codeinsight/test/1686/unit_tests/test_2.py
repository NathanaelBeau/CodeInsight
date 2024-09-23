arr0 = np.array([[0.5, 1.5], [2.5, 3.5], [4.5, 5.5]])
row0 = np.array([2.5, 3.5])
expected_result =  True
result = test(arr0, row0)
assert result == expected_result, 'Test failed'