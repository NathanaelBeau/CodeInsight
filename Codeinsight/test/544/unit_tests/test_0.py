dict0 = {'a': 10, 'b': 20, 'c': 30}
expected_output = pd.DataFrame([('a', 10), ('b', 20), ('c', 30)], columns=['key', 'value'])
assert test(dict0).values.tolist()  ==expected_output.values.tolist() , 'Test failed'