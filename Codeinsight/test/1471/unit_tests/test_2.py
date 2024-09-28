data = {'Amazon': [0, 173, 0],
        'Apple': [0, 0, 130],
        'Yahoo': [150, 0, 0]}
index_values = ['Z', 'C', 'A']
df0 = pd.DataFrame(data, index=index_values)
lst0 = ["A", "Z", "C"]
expected_output = df0.reindex(lst0)
assert test(df0, lst0) .equals( expected_output), 'Test failed'