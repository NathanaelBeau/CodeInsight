df = pd.DataFrame(columns=['Category', 'Values'])
result = test(df, 'Category', 'Values')
expected = pd.DataFrame(columns=['Category', 'Values'])
assert result.equals(expected), 'Test failed'