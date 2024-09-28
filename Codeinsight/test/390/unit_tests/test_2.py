dict0 = {'a': -1, 'b': -2, 'c': -3}
result = test(dict0, lambda x: x > 0)
assert result ==0, 'Test failed'