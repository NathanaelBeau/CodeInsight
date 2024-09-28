lst0 = [{'name': 'David', 'score': 95},
        {'name': 'Eve', 'score': 88},
        {'name': 'Frank', 'score': 92}]
var0 = 'name'
expected_output = {'David': {'score': 95},
                   'Eve': {'score': 88},
                   'Frank': {'score': 92}}
assert test(lst0, var0) == expected_output, 'Test failed'