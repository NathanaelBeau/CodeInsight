df0 = pd.DataFrame({'A': ['-', 'Value1', '-'],
                            'B': ['Value2', '-', 'Value3']})
expected_output = pd.DataFrame({'A': [None, 'Value1', None],
                                        'B': ['Value2', None, 'Value3']})
assert test(df0) .equals(expected_output), 'Test failed'