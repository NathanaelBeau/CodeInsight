lst0 = [{'name': 'John', 'age': 30, 'city': 'New York'},
        {'name': 'Alice', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Bob', 'age': 35, 'city': 'Chicago'}]
var0 = 'name'
expected_output = {'John': {'age': 30, 'city': 'New York'},
                   'Alice': {'age': 25, 'city': 'Los Angeles'},
                   'Bob': {'age': 35, 'city': 'Chicago'}}
assert test(lst0, var0) == expected_output, 'Test failed'