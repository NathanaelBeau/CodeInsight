class MyObject:
    def __init__(self, resultType):
        self.resultType = resultType
obj1 = MyObject("A")
obj2 = MyObject("C")
obj3 = MyObject("B")
lst0 = [obj3, obj1, obj2]
expected_output = [obj1, obj3, obj2]
output = test(lst0)
assert output == expected_output, 'Test failed'