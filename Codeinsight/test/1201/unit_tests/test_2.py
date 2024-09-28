df0 = pd.DataFrame({'lib': ['C'], 'qty1': [5], 'qty2': [6]})
dict0 = {'lib': 'D', 'qty1': 7, 'qty2': 8}
expected_output = pd.DataFrame({'lib': ['C', 'D'], 'qty1': [5, 7], 'qty2': [6, 8]})
assert test(df0, dict0) .equals(expected_output), 'Test failed'