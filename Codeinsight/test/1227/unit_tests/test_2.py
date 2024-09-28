class MyClass:
    def __init__(self, my_attr):
        self.my_attr = my_attr
lst0 = [MyClass(True), MyClass(False), MyClass(True)]
expected_result =  [True, False, True]
assert test(lst0) == expected_result, 'Test failed'