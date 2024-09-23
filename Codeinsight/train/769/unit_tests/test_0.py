dict0 = {'a': [1, 2, 3], 'b': [4, 5, 6]}
expected_result =  np.array([('a', [1, 2, 3]), ('b', [4, 5, 6])],
                           dtype=[('name', 'U10'), ('value', '3int16')])
result = test(dict0)
assert (result  ==  expected_result).all(), 'Test failed'