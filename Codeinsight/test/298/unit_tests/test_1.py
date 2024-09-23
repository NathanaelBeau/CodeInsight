df0 = pd.DataFrame(columns=['A', 'B'])
expected = np.array([])
result = test(df0)
assert (result == expected).all(), 'Test failed'