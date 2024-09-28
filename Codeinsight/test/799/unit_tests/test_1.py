var0 = pd.DataFrame({'variable': ['apple', 'banana', 'apple', 'orange', 'banana']})
expected_output = pd.DataFrame({'variable': ['apple', 'banana', 'orange'], 'counts': [2, 2, 1]})
assert test(var0).equals(expected_output), 'Test failed'