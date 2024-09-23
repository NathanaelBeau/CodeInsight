col = pd.MultiIndex.from_arrays([['one', 'one', 'one', 'two', 'two', 'two'],
                                ['a', 'b', 'c', 'a', 'b', 'c']])
df = pd.DataFrame(columns=col)
expected_result =  df.drop(columns=[('one', 'b'), ('two', 'b')])
result = test('a', 'c', 'one', 'two', df)
assert result.equals(expected_result), 'Test failed'