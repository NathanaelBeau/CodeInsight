lst1 = [{"name": "John", "age": 25}, {"name": "Jane", "age": 30}, {"name": "John", "age": 25}]
expected_result1 = [{"name": "John", "age": 25}, {"name": "Jane", "age": 30}]
assert test(lst1) == expected_result1, 'Test failed'