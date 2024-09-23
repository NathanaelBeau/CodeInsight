col0 = 'name'
df0 = pd.DataFrame({'name': ['john', 'jane', 'mike']})
expected_output = pd.DataFrame({'name': ['JOHN', 'JANE', 'MIKE']})
assert test(df0, col0).equals(expected_output), 'Test failed'