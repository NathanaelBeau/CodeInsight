def generator1():
    for i in range(10):
        yield i
result1 = test(generator1(), 5)
assert result1 == [0, 1, 2, 3, 4], 'Test failed'