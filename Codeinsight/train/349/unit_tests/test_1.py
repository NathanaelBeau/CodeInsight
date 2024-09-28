df0 = pd.DataFrame({'A': ['apple', 'banana'], 'B': ['carrot', 'date']})
expected_output = ['apple', 'carrot', 'banana', 'date']
assert np.array_equal(test(df0) , (expected_output)), 'Test failed'