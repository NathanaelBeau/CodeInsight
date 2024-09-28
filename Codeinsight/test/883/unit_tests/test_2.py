lst0 = [
    {'categories': ['A', 'B', 'B']},
    {'categories': ['A', 'C', 'D']},
    {'categories': ['B', 'C', 'C']}
]
expected_output = {'B': 3, 'C': 3, 'A': 2, 'D': 1}
assert test(lst0) == expected_output, 'Test failed'