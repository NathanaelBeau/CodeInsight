data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}
df0 = pd.DataFrame(data)
expected_output = pd.Series([8.124038, 9.643651, 11.224972])
test_result = test(df0)
assert np.allclose(test_result, expected_output), 'Test failed'