df = pd.DataFrame(columns=['Name', 'Priority'])
priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
result = test(df, 'Priority', priority_order)
expected = pd.DataFrame(columns=['Name', 'Priority'])
assert result.equals(expected), 'Test failed'