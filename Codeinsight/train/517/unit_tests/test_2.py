df0 = pd.DataFrame({
            'A': [1, 2, 3]
        })
expected = np.array([1, 2, 3])
result = test(df0)
assert (result == expected).all(), 'Test failed'