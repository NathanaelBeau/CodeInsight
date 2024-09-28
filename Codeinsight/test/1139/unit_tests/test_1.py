df_test = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 15, 20, 25, 30]
})
result = test(df_test, 'A', 0, 5)
expected = pd.Series([True, True, True, True, True], name='A')

assert result.equals(expected), 'Test failed'