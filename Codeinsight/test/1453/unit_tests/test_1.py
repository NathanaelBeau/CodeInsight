arr0 = np.array([[10, 20], [30, 40], [50, 60]])
row0 = np.array([70, 80])
expected_result =  False
result = test(arr0, row0)
assert result == expected_result, 'Test failed'