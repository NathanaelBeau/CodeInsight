dict0 = {'p': [13, 14, 15], 'q': [16, 17, 18]}
expected_result =  np.array([('p', [13, 14, 15]), ('q', [16, 17, 18])],
                           dtype=[('name', 'U10'), ('value', '3int16')])
result = test(dict0)
assert (result  ==  expected_result).all(), 'Test failed'