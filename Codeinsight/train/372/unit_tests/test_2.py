result = test()
assert all(isinstance(item, float) for item in result), 'Test failed'