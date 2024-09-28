df_test = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 15, 20, 25, 30]
})

# Test for values in column 'A' between 2 and 4
result = test(df_test, 'A', 2, 4)
expected = pd.Series([False, True, True, True, False], name='A')

assert result.equals(expected), 'Test failed'
