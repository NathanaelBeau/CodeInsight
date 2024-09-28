lst0 = [
    {'categories': ['A', 'B', 'C']},
    {'categories': ['A', 'C', 'D']},
    {'categories': ['B', 'C', 'C']}
]
expected_output = {'C': 4, 'A': 2, 'B': 2, 'D': 1}
assert test(lst0) ==expected_output, 'Test failed'