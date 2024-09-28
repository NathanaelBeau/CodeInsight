df0 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                            'count': [10, 15, 20, 25]})
df1 = pd.DataFrame({'key': ['C', 'D', 'E', 'F'],
                            'count': [20, 25, 30, 35]})
var0 = 'key'
expected_output = pd.DataFrame({'key': ['C', 'D'],
                                        'count_x': [20, 25],
                                        'count_y': [20, 25]})
assert test(df0, df1, var0) .equals(expected_output), 'Test failed'