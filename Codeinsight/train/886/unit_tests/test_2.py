import numpy as np
col = pd.MultiIndex.from_arrays([['one', 'one', 'one', 'two', 'two', 'two'],
                                ['a', 'b', 'c', 'a', 'b', 'c']])
df = pd.DataFrame(columns=col)
values = np.array([[1, 2, 3, 4, 5, 6]])
df.loc[0] = values[0]
expected_result =  df.drop(columns=[('one', 'b'), ('two', 'b')])
result = test('a', 'c', 'one', 'two', df)
assert result.equals(expected_result), 'Test failed'