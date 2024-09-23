lst0 = [
    [{'play': 1}],
    [{'play': 2}, {'play': 3}],
    [{'play': 4}, {'play': 5}, {'play': 6}],
    [{'play': 7}, {'play': 8}, {'play': 9}, {'play': 10}]
]
expected_output = [
    [{'play': 7}, {'play': 8}, {'play': 9}, {'play': 10}],
    [{'play': 4}, {'play': 5}, {'play': 6}],
    [{'play': 2}, {'play': 3}],
    [{'play': 1}]
]
assert test(lst0) == expected_output, 'Test failed'