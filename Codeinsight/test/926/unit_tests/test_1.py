def generator3():
    for i in range(10):
        yield i**2
result3 = test(generator3(), 4)
assert result3 == [0, 1, 4, 9], 'Test failed'