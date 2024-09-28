data = {'A': [4, 2, 7],
        'B': [1, 5, 3],
        'C': [8, 6, 9]}
df0 = pd.DataFrame(data)
expected_output = pd.Series([9.000000, 8.062258, 11.789826])
test_result = test(df0)
assert np.allclose(test_result, expected_output), 'Test failed'