lst0 = [
    {'categories': ['A', 'B', 'C']},
    {'categories': ['A', 'A', 'D']},
    {'categories': ['B', 'C', 'C']}
]
expected_output = {'A': 3, 'C': 3, 'B': 2, 'D': 1}
assert test(lst0)== expected_output, 'Test failed'