dict0 = {'x': [7, 8, 9], 'y': [10, 11, 12]}
expected_result =  np.array([('x', [7, 8, 9]), ('y', [10, 11, 12])],
                           dtype=[('name', 'U10'), ('value', '3int16')])
result = test(dict0)
assert (result  ==  expected_result).all(), 'Test failed'