lst0 = [
    [{'play': 2}, {'play': 1}],
    [{'play': 4}, {'play': 6}],
    [{'play': 3}, {'play': 5}],
]
expected_output = [
    [{'play': 4}, {'play': 6}],
    [{'play': 3}, {'play': 5}],
    [{'play': 2}, {'play': 1}]
]
assert test(lst0) == expected_output, 'Test failed'