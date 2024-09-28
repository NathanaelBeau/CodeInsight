df0 = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
expected = np.array([1, 4, 2, 5, 3, 6])
result = test(df0)
assert (result == expected).all(), 'Test failed'