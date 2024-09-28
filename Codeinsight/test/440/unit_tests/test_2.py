df0 = pd.DataFrame({
    'A': [1.5, 2.5, 3.5],
    'B': [4.5, 5.5, 6.5]
})
df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
expected = pd.DataFrame({
    'A': [0.5, 0.5, 0.5],
    'B': [0.5, 0.5, 0.5]
})

result = test(df0, df1)
assert result.equals(expected), 'Test failed'