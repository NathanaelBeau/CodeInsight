df0 = pd.DataFrame({'user_id': [1, 2, 3, 4, 5],
                            'data': ['A', 'B', 'C', 'D', 'E']})
df1 = pd.DataFrame({'user_id': [3, 4, 5, 6, 7],
                            'data': ['C', 'D', 'E', 'F', 'G']})
var0 = 'user_id'
expected_output = pd.DataFrame({'user_id': [3, 4, 5],
                                        'data_x': ['C', 'D', 'E'],
                                        'data_y': ['C', 'D', 'E']})
assert test(df0, df1, var0) .equals(expected_output), 'Test failed'