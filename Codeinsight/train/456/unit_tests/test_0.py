lst0 = [1, 2, 1, 3]
lst1 = ['a', 'b', 'a', 'c']
expected_codes = pd.Series([0, 1, 0, 2], dtype='int8')
result = pd.Series(test('col1', 'col2', lst0, lst1))
assert result.equals(expected_codes), 'Test failed'