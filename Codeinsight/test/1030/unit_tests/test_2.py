def generator2():
    for i in range(3):
        yield i
result2 = test(generator2(), 5)
assert result2 == [0, 1, 2], 'Test failed'