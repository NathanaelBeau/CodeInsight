df0 = pd.DataFrame({'A': ['-', 'Value1', '-', 'Value2', 'Value3'],
                            'B': ['Value4', '-', 'Value5', '-', 'Value6']})
expected_output = pd.DataFrame({'A': [None, 'Value1', None, 'Value2', 'Value3'],
                                    'B': ['Value4', None, 'Value5', None, 'Value6']})
assert test(df0) .equals(expected_output), 'Test failed'