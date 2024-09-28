df0 = pd.DataFrame({'stats': ["(10,20,30)", "(40,50,60)", "(70,80,90)"]})
var0 = 'stats'
expected_output = pd.DataFrame({'col1': [10.0, 40.0, 70.0],
                                'col2': [20.0, 50.0, 80.0],
                                'col3': [30.0, 60.0, 90.0]})
assert test(df0, var0).values.tolist() == expected_output.values.tolist(), 'Test failed'