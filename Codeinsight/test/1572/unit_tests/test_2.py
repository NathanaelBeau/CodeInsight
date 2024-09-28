lst0 = [{'key': 'first', 'age': 25}, {'key': 'second', 'age': 30}]
expected_result =  {'first': {'key': 'first', 'age': 25}, 'second': {'key': 'second', 'age': 30}}
assert test(lst0) == expected_result, 'Test failed'