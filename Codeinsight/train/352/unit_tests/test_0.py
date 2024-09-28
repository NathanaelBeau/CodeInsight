lst0 = [
    ('a', 1),
    ('a', 2),
    ('a', 3),
    ('b', 1),
    ('b', 2),
    ('c', 1),
]
expected_output = { 'a': [1, 2, 3], 'b': [1, 2], 'c': [1] }
assert test(lst0) ==expected_output, 'Test failed'