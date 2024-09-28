df = pd.DataFrame(columns=['test1', 'test2'])
assert test('test1', 'test2', df).empty, 'Test failed'