df = pd.DataFrame({'var0': [1, 1, 2, 2], 'var1': ['a', 'a', 'b', 'b']})
assert test('var0', 'var1', df).equals(pd.DataFrame({'var0': [1, 2], 'var1': ['a', 'b'], 'frequency': [2, 2]})), 'Test failed'