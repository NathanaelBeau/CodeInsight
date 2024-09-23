var0 = 2
lst0 = [('John', 30, {'city': 'New York'}), ('Jane', 25, {'city': 'London'}), ('Mike', 40, {'city': 'Paris'})]
expected_result =  [{'city': 'New York'}, {'city': 'London'}, {'city': 'Paris'}]
result = test(var0, lst0)
assert result == expected_result, 'Test failed'