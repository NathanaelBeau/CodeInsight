class MyClass:
    def __init__(self, my_attr):
        self.my_attr = my_attr
lst0 = [MyClass("a"), MyClass("b"), MyClass("c")]
expected_result =  ["a", "b", "c"]
assert test(lst0) == expected_result, 'Test failed'