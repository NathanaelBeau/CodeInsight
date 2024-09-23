lst0 = [1, 1, 1, 1]
lst1 = ['a', 'a', 'a', 'a']
expected_codes = pd.Series([0, 0, 0, 0], dtype='int8')
result = pd.Series(test('col1', 'col2', lst0, lst1))
assert result.equals(expected_codes), 'Test failed'