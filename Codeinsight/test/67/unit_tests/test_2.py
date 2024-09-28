d3 = {'key1': ['apple', 'banana'], 'key2': ['fruit', 'fruit']}
expected_output3 = [{'key1': 'apple', 'key2': 'fruit'}, {'key1': 'banana', 'key2': 'fruit'}]
assert test(d3) == expected_output3, 'Test failed'