var0 = pd.DataFrame({'variable': ['apple', 'banana', 'apple', 'orange', 'banana']})
expected_output = pd.Series({'banana': 2, 'apple': 2, 'orange': 1}, name='variable').sort_index()
assert test(var0).sort_index().equals(expected_output), 'Test failed'