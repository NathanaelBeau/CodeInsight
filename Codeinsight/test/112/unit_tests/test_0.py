class TestClass:
    def __init__(self, x_value):
        self.x = x_value
obj1 = TestClass(5)
assert test(obj1) == 5, 'Test failed'