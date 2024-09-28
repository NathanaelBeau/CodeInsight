class MyClass:
    def __init__(self, my_attr):
        self.my_attr = my_attr
lst0 = [MyClass(1), MyClass(2), MyClass(3)]
expected_result =  [1, 2, 3]
assert test(lst0) == expected_result, 'Test failed'