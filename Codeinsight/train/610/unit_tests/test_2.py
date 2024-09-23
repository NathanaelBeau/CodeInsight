data = {'A': [3, 6, 9],
        'B': [2, 5, 8],
        'C': [1, 4, 7]}
df0 = pd.DataFrame(data)
expected_output = pd.Series([3.741657, 8.774964, 13.928388])
test_result = test(df0)
assert np.allclose(test_result, expected_output), 'Test failed'