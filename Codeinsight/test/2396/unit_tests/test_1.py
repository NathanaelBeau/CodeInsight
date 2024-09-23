arr0 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
lst0 = [0, 2]
lst1 = [0, 2]
expected_result =  np.array([[50]])
result = test(arr0, lst0, lst1)
assert np.array_equal(result, expected_result), 'Test failed'