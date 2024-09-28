class TestClass:
    def __init__(self, x_value):
        self.x = x_value
obj3 = TestClass([1, 2, 3])
assert test(obj3) == [1, 2, 3], 'Test failed'