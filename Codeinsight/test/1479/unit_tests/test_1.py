result = test()
assert all(0.0 <= item <= 1.0 for item in result), 'Test failed'