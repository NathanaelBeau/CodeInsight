df_test_4 = pd.DataFrame({
    'A': [1, 2],
    'B': ['x,y', None],
    'C': [3, 4]
})
result_4 = test(df_test_4, 'B', ',', ['A', 0, 1, 'C'])
expected_4 = pd.DataFrame({'A': [1, 2], 0: ['x', None], 1: ['y', None], 'C': [3, 4]})
assert result_4.equals(expected_4), 'Test failed'