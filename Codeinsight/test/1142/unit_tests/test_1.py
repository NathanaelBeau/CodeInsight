df0 = pd.DataFrame({'X': [10, 20, 30], 'Y': [40, 50, 60], 'Z': [70, 80, 90]})
lst0 = ['X', 'Z']
expected_result =  np.array([[10, 70], [20, 80], [30, 90]])
result = test(df0, lst0)
assert np.array_equal(result, expected_result), 'Test failed'