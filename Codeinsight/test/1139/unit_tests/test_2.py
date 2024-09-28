df_test = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 15, 20, 25, 30]
})

result = test(df_test, 'B', 15, 25)
expected = pd.Series([False, True, True, True, False], name='B')

assert result.equals(expected), 'Test failed'