lst0 = [
    ('a', 1),
    ('a', 2),
    ('b', 3),
    ('b', 4),
    ('b', 5)
]
expected_output = { 'a': [1, 2], 'b': [3, 4, 5] }
assert test(lst0) ==expected_output, 'Test failed'