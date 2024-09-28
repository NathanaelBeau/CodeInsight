import pandas as pd
def test(lst0, lst1):
    df_grouped = lst0.groupby(lst1).size()
    return df_grouped
# Test unitaire
lst0 = pd.DataFrame({ 'col2': ['A', 'B', 'A', 'B', 'A'], 'col5': [1, 2, 2, 1, 1] })
lst1 = ['col5', 'col2']
expected_output = pd.Series([2, 1, 1, 1], index=pd.MultiIndex.from_tuples([(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]))
assert test(lst0, lst1).equals(expected_output), 'Test failed'