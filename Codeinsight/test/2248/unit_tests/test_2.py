dict0 = {'x': 3.14, 'y': 2.71, 'z': 1.618}
expected_output = pd.DataFrame([('x', 3.14), ('y', 2.71), ('z', 1.618)], columns=['key', 'value'])
assert test(dict0).values.tolist()  ==expected_output.values.tolist() , 'Test failed'