str0 = "{'fruit': 'apple', 'color': 'red'}"
expected_result =  {'fruit': 'apple', 'color': 'red'}
result = test(str0)
assert result == expected_result, 'Test failed'