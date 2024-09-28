lst0 = [
    [{'play': 5}, {'play': 3}, {'play': 1}],
    [{'play': 4}, {'play': 2}],
    [{'play': 6}, {'play': 8}, {'play': 7}]
]
expected_output = [
    [{'play': 6}, {'play': 8}, {'play': 7}],
    [{'play': 5}, {'play': 3}, {'play': 1}],
    [{'play': 4}, {'play': 2}]
]
assert test(lst0) == expected_output, 'Test failed'