class Item:
    def __init__(self, name, age):
        self.name = name
        self.age = age
lst0 = [Item("Alice", 25), Item("Bob", 30), Item("Charlie", 25)]
var0 = 25
attr_name = "age"
expected_result =  [lst0[0], lst0[2]]
assert test(lst0, var0, attr_name) == expected_result, 'Test failed'