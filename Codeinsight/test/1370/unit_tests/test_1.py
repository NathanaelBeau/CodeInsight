df_test_2 = pd.DataFrame({
    'A': [1, 2],
    'B': ['x', 'z'],
    'C': [3, 4]
})
result_2 = test(df_test_2, 'B', ',', ['A', 0, 'C'])
expected_2 = pd.DataFrame({'A': [1, 2], 0: ['x', 'z'], 'C': [3, 4]})
assert result_2.equals(expected_2),  'Test failed'