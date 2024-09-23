# Unit Tests for Excluding
df0 = pd.DataFrame({ 'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9] })
lst0 = ['A', 'B']
expected_result_exclude = pd.DataFrame({'C': [7, 8, 9]})
result_exclude = test(df0, lst0)
assert result_exclude.equals(expected_result_exclude), 'Test failed'