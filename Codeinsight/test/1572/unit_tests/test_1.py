lst0 = [{'key': 'x', 'data': 100}, {'key': 'y', 'data': 200}]
expected_result =  {'x': {'key': 'x', 'data': 100}, 'y': {'key': 'y', 'data': 200}}
assert test(lst0) == expected_result, 'Test failed'