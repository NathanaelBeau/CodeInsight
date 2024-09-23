# Unit Test 3 for Excluding
df0 = pd.DataFrame({ 'P': [19, 20, 21], 'Q': [22, 23, 24], 'R': [25, 26, 27] })
lst0 = ['Q']
expected_result_exclude_3 = pd.DataFrame({'P': [19, 20, 21], 'R': [25, 26, 27]})
result_exclude_3 = test(df0, lst0)
assert result_exclude_3.equals(expected_result_exclude_3), 'Test failed'