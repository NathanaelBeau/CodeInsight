df0 = pd.DataFrame({'M': ['m', 'n', 'm', 'n'], 'N': ['o', 'o', 'p', 'p'], 'O': ['q', 'q', 'r', 'r']})
lst0 = ['M', 'O']
expected_result3 = pd.DataFrame({'M': ['m', 'm', 'n', 'n'], 'O': ['q', 'r', 'q', 'r'], 'var0': [1, 1, 1, 1]})
result3 = test(df0, lst0)
assert result3.equals(expected_result3), 'Test failed'