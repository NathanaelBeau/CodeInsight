lst0 = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]
var0 = 'age'
reverse = True
expected_output = [{'name': 'Alice', 'age': 30}, {'name': 'John', 'age': 25}, {'name': 'Bob', 'age': 20}]
assert test(lst0, var0, reverse) ==expected_output, 'Test failed'