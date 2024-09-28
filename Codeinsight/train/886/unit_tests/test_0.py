import numpy as np
col = pd.MultiIndex.from_arrays([['one', 'one', 'one', 'two', 'two', 'two'],
                                ['a', 'b', 'c', 'a', 'b', 'c']])
# Create an empty DataFrame with the specified column structure
df = pd.DataFrame(columns=col)
# Define the values to fill the DataFrame
values = np.array([[1, 2, 3, 4, 5, 6],
                   [7, 8, 9, 10, 11, 12]])
# Assign the values to the DataFrame
df.loc[0] = values[0]
df.loc[1] = values[1]
expected_result =  df.drop(columns=[('one', 'b'), ('two', 'b')])
result = test('a', 'c', 'one', 'two', df)
assert result.equals(expected_result), 'Test failed'