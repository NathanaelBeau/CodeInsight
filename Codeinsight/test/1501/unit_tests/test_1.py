df0 = pd.DataFrame({'stats': ["(0.1,0.2,0.3)", "(0.4,0.5,0.6)", "(0.7,0.8,0.9)"]})
var0 = 'stats'
expected_output = pd.DataFrame({'col1': [0.1, 0.4, 0.7],
                                'col2': [0.2, 0.5, 0.8],
                                'col3': [0.3, 0.6, 0.9]})
assert test(df0, var0).values.tolist() == expected_output.values.tolist(), 'Test failed'