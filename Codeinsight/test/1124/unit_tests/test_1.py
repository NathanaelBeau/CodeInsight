lst0 = pd.DataFrame({ 'col2': ['A', 'A', 'B', 'B', 'A'], 'col5': [1, 1, 2, 2, 1] })
lst1 = ['col5', 'col2']
expected_output = pd.Series([3, 2], index=pd.MultiIndex.from_tuples([(1, 'A'), (2, 'B')]))
assert test(lst0, lst1).equals(expected_output), 'Test failed'