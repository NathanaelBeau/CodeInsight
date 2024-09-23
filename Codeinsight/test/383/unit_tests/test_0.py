lst0 = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 20}]
var0 = 'age'
reverse=False
expected_output = [{'name': 'Bob', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}]
assert test(lst0, var0, reverse) ==expected_output, 'Test failed'