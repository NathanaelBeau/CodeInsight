class TestClass:
    def __init__(self, x_value):
        self.x = x_value
obj2 = TestClass("hello")
assert test(obj2) == "hello", 'Test failed'