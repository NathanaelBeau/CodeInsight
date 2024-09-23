dict0 = {'a': 'hello', 'b': 'world', 'c': 'python'}
expected_output = pd.DataFrame([('a', 'hello'), ('b', 'world'), ('c', 'python')], columns=['key', 'value'])
assert test(dict0).values.tolist()  ==expected_output.values.tolist() , 'Test failed'