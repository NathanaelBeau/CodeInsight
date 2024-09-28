dict0 = {'a': 10, 'b': 15, 'c': 5, 'd': 20}
result = test(dict0, lambda x: x > 10)
assert result ==2, 'Test failed'