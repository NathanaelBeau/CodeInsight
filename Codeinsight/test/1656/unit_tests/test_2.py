class Item:
    def __init__(self, name, age):
        self.name = name
        self.age = age
lst0 = [Item("Alice", "Engineer"), Item("Bob", "Doctor"), Item("Charlie", "Engineer")]
var0 = "Engineer"
attr_name = "name"
expected_result =  []
assert test(lst0, var0, attr_name) == expected_result, 'Test failed'