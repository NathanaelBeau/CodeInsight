df0 = pd.DataFrame({'id': [101, 102, 103],
                            'value': [10, 20, 30]})
df1 = pd.DataFrame({'id': [102, 103, 104],
                            'value': [20, 30, 40]})
var0 = 'id'
expected_output = pd.DataFrame({'id': [102, 103],
                                        'value_x': [20, 30],
                                        'value_y': [20, 30]})
assert test(df0, df1, var0) .equals(expected_output), 'Test failed'